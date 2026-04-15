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

# import pandas as pd
#
#
# class CourseReference:
#     def __init__(self, courses_path):
#         # Файлды оқимыз
#         self.df = pd.read_csv(courses_path, skipinitialspace=True)
#         # Баған аттарын тазарту
#         self.df.columns = self.df.columns.str.strip()
#
#     def prepare_reference(self):
#         # 1. 'course_code' бағанындағы дубликаттарды жою
#         # keep='first' — бірінші кездескенін қалдырып, қалғандарын өшіреді
#         self.df = self.df.drop_duplicates(subset=['course_code'], keep='first')
#
#         # 2. 'course_code' бойынша сұрыптау
#         self.df = self.df.sort_values(by='course_code')
#
#         return self.df
#
#
# # Бағдарламаны іске қосу
# if __name__ == "__main__":
#     try:
#         task10 = CourseReference('courses.csv')
#         cleaned_df = task10.prepare_reference()
#
#         print("10-тапсырма: Тазартылған және сұрыпталған анықтамалық:")
#         print(cleaned_df)
#
#         # Нәтижені тексеру үшін жаңа файлға сақтап қоюға болады
#         # cleaned_df.to_csv('courses_cleaned.csv', index=False)
#
#     except Exception as e:
#         print(f"Қате: {e}")