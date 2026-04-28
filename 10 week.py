import pandas as pd

class CourseManager:
    def __init__(self, enroll_path, courses_path):
        self.enroll = pd.read_csv(enroll_path)
        self.courses = pd.read_csv(courses_path)

    def process_data(self):
        self.courses = self.courses.drop_duplicates(subset=['course_code']).sort_values('course_code')

        merged_df = pd.merge(self.enroll, self.courses, on='course_code')
        return merged_df.groupby('title')['student_id'].count().reset_index()

if __name__ == "__main__":
    task10 = CourseManager('enroll.csv', 'courses.csv')
    result = task10.process_data()
    print("Студенттер саны (курстар бойынша):")
    print(result)