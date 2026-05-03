import json
from CourseIntersection import CourseIntersection
from CourseManager import CourseManager
from CourseMerger import CourseMerger
from CourseAnalytics import CourseAnalytics
from CourseVisualizer import CourseVisualizer

if __name__ == "__main__":
    try:
        print("=" * 40)
        print("  КУРС ЖОБАСЫ: ДЕРЕКТЕРДІ ТАЛДАУ  ")
        print("=" * 40)

        # --- 9-апта: Кодтардың қиылысуы ---
        task9 = CourseIntersection('enroll.csv', 'courses.csv')
        result9 = task9.get_intersection()
        print(f"\n[9-апта] Ортақ кодтар тізімі:\n{result9}")

        # --- 10-апта: Справочникті тазарту ---
        task10 = CourseManager('enroll.csv', 'courses.csv')
        # Ескерту: Файлыңдағы функция аты process_data екеніне көз жеткіз
        cleaned_df = task10.process_data()
        print(f"\n[10-апта] Справочник тазартылды. Жазба саны: {len(cleaned_df)}")

        # --- 11-апта: Мәліметтерді біріктіру ---
        task11 = CourseMerger('enroll.csv', 'courses.csv')
        merged_df = task11.perform_merge()
        print(f"\n[11-апта] Мәліметтер біріктірілді. Алғашқы 3 жол:")
        print(merged_df.head(3))

        # --- 12-апта: Аналитика және сақтау ---
        task12 = CourseAnalytics('enroll.csv', 'courses.csv')
        analytics_result = task12.get_top_courses()
        print("\n[12-апта] Уникалды студенттер саны (Топ курстар):")
        print(analytics_result)

        # --- 13-апта: Визуализация ---
        print("\n[13-апта] График дайындалуда... (Терезені жапқанда жалғасады)")
        task13 = CourseVisualizer('top_courses.csv')
        task13.draw_top_chart()

        # --- 14-апта: JSON форматына экспорттау (Қорытынды) ---
        print("\n[14-апта] Деректерді JSON форматына айналдыру...")
        # DataFrame-ді сөздікке айналдырып, JSON ретінде шығарамыз
        json_data = analytics_result.to_json(orient='records', force_ascii=False)
        formatted_json = json.dumps(json.loads(json_data), indent=4, ensure_ascii=False)

        with open('final_report.json', 'w', encoding='utf-8') as f:
            f.write(formatted_json)

        print("Қорытынды JSON есебі 'final_report.json' файлына сақталды!")
        print("      ЖОБА АЯҚТАЛДЫ!      ")

    except KeyError as e:
        print(f"\n[Қате]: Баған табылмады: {e}. CSV файлдарын тексеріңіз.")
    except Exception as e:
        print(f"\n[Күтпеген қате]: {e}")