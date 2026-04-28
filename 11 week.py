import pandas as pd

class CourseMerger:
    def __init__(self, enroll_path, courses_path):
        self.enroll = pd.read_csv(enroll_path, skipinitialspace=True)
        self.courses = pd.read_csv(courses_path, skipinitialspace=True)

        self.enroll.columns = self.enroll.columns.str.strip()
        self.courses.columns = self.courses.columns.str.strip()

    def perform_merge(self):
        courses_cleaned = self.courses.drop_duplicates(subset=['course_code'])

        merged_df = pd.merge(self.enroll, courses_cleaned, on='course_code', how='inner')

        return merged_df

if __name__ == "__main__":
    try:
        task11 = CourseMerger('enroll.csv', 'courses.csv')
        result_df = task11.perform_merge()

        print("11-тапсырма: Біріктірілген кесте (Merge):")
        print(result_df.head())

        print(f"\nБарлығы {len(result_df)} жазба біріктірілді.")

    except Exception as e:
        print(f"Қате орын алды: {e}")