import pandas as pd

class CourseAnalytics:
    def __init__(self, enroll_path, courses_path):
        self.enroll = pd.read_csv(enroll_path, skipinitialspace=True)
        self.courses = pd.read_csv(courses_path, skipinitialspace=True)
        self.enroll.columns = self.enroll.columns.str.strip()
        self.courses.columns = self.courses.columns.str.strip()

    def get_top_courses(self):
        courses_cleaned = self.courses.drop_duplicates(subset=['course_code'])
        merged_df = pd.merge(self.enroll, courses_cleaned, on='course_code')

        result = merged_df.groupby('title')['student_id'].nunique().reset_index()

        result = result.sort_values(by='student_id', ascending=False)

        result.to_csv('top_courses.csv', index=False)

        return result


if __name__ == "__main__":
    try:
        analytics = CourseAnalytics('enroll.csv', 'courses.csv')
        top_courses = analytics.get_top_courses()

        print("12-тапсырма: Курстар бойынша уникалды студенттер саны:")
        print(top_courses)
        print("\nНәтиже 'top_courses.csv' файлына сақталды.")

    except Exception as e:
        print(f"Қате: {e}")