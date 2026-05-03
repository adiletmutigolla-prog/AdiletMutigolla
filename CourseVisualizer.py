import pandas as pd
import matplotlib.pyplot as plt


class CourseVisualizer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def draw_top_chart(self):
        top_7 = self.df.head(7).copy()

        top_7 = top_7.sort_values(by='student_id', ascending=True)

        plt.figure(figsize=(10, 6))

        bars = plt.barh(top_7['title'], top_7['student_id'], color='orchid')

        plt.xlabel('Студенттер саны')
        plt.ylabel('Курс атауы')
        plt.title('Ең танымал 7 курс')

        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
                     f' {int(bar.get_width())}', va='center')

        plt.tight_layout()

        plt.savefig('top_courses_chart.png')
        print("График 'top_courses_chart.png' файлына сақталды!")

        plt.show()


if __name__ == "__main__":
    try:
        visualizer = CourseVisualizer('top_courses.csv')
        visualizer.draw_top_chart()
    except Exception as e:
        print(f"График шығару кезінде қате кетті: {e}")
        print("Алдымен 12-аптаның кодын іске қосып, 'top_courses.csv' файлын жасап алыңыз.")