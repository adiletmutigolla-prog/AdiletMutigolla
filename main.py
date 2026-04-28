import pandas as pd


def create_project_files():
    # 1. enroll.csv үшін деректер (Студенттер тізімі)
    enroll_data = {
        'course_code': [
            'CS101', 'CS101', 'MATH202', 'CS101', 'MATH202',
            'PHYS303', 'PYTHON1', 'PYTHON1', 'DB202', 'DB202',
            'AI404', 'AI404', 'ENG101', 'CS101', 'DB202'
        ],
        'student_id': [
            101, 102, 103, 104, 105,
            106, 107, 108, 109, 110,
            111, 112, 113, 114, 115
        ]
    }

    # 2. courses.csv үшін деректер (Курстар анықтамалығы)
    # Мұнда әдейі бір курсты (CS101) екі рет жаздық, 10-тапсырма дубликатты жою үшін
    courses_data = {
        'course_code': [
            'CS101', 'MATH202', 'PHYS303', 'PYTHON1',
            'DB202', 'AI404', 'ENG101', 'CS101'
        ],
        'title': [
            'Python Programming', 'Calculus', 'General Physics', 'Advanced Python',
            'Database Systems', 'Artificial Intelligence', 'Academic English', 'Python Programming'
        ]
    }

    # DataFrame жасау
    enroll_df = pd.DataFrame(enroll_data)
    courses_df = pd.DataFrame(courses_data)

    # CSV файлдарына сақтау
    # index=False — артық сандар бағанын қоспау үшін
    # encoding='utf-8' — қазақ/орыс әріптері дұрыс көрінуі үшін
    enroll_df.to_csv('enroll.csv', index=False, encoding='utf-8')
    courses_df.to_csv('courses.csv', index=False, encoding='utf-8')

    print("Файлдар сәтті жасалды: enroll.csv және courses.csv")
    print("Енді негізгі кодты (9-14 апта) іске қоса берсеңіз болады!")


if __name__ == "__main__":
    create_project_files()