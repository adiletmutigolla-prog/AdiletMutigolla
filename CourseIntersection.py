import pandas as pd

class CourseIntersection:
    def __init__(self, enroll_path, courses_path):
        self.enroll = pd.read_csv(enroll_path, skipinitialspace=True)
        self.courses = pd.read_csv(courses_path, skipinitialspace=True)

        self.enroll.columns = self.enroll.columns.str.strip()
        self.courses.columns = self.courses.columns.str.strip()

    def get_intersection(self):
        codes_enroll = set(self.enroll['course_code'].astype(str).str.strip().unique())
        codes_courses = set(self.courses['course_code'].astype(str).str.strip().unique())

        return sorted(list(codes_enroll & codes_courses))

if __name__ == "__main__":
    try:
        task9 = CourseIntersection('enroll.csv', 'courses.csv')
        result = task9.get_intersection()
        print("9-тапсырма нәтижесі (Ортақ кодтар):")
        print(result)
    except KeyError:
        print("Қате: 'course_code' бағаны табылмады. CSV файлдарын тексеріңіз.")
    except Exception as e:
        print(f"Күтпеген қате: {e}")