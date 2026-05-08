import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import uvicorn


class CourseIntersection:
    def __init__(self, e_path, c_path):
        self.enroll = pd.read_csv(e_path)
        self.courses = pd.read_csv(c_path)

    def get_intersection(self):
        e_codes = set(self.enroll['course_code'].astype(str).str.strip())
        c_codes = set(self.courses['course_code'].astype(str).str.strip())
        return sorted(list(e_codes & c_codes))


class CourseAnalytics:
    def __init__(self, e_path, c_path):
        self.enroll = pd.read_csv(e_path)
        self.courses = pd.read_csv(c_path)

    def get_top_courses(self):
        c_clean = self.courses.drop_duplicates(subset=['course_code'])
        merged = pd.merge(self.enroll, c_clean, on='course_code')
        result = merged.groupby('title')['student_id'].nunique().reset_index()
        result = result.sort_values(by='student_id', ascending=False)
        result.to_csv('top_courses.csv', index=False)
        return result


class CourseVisualizer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def draw_top_chart(self):
        top_7 = self.df.head(7).copy().sort_values(by='student_id', ascending=True)
        plt.figure(figsize=(10, 6))
        bars = plt.barh(top_7['title'], top_7['student_id'], color='green')
        plt.title('Ең танымал 7 курс')
        for bar in bars:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f' {int(bar.get_width())}', va='center')
        plt.tight_layout()
        plt.savefig('top_courses_chart.png')
        plt.close()


app = FastAPI(title="Оқу курстарын талдау жүйесі")


@app.get("/")
def home():
    return {
        "Жоба": "Курстар деректерін талдау",
        "Қолжетімді жолдар": {
            "/analyze": "9-12 апта тапсырмаларын орындау",
            "/chart": "13-апта: Графикті көру",
            "/report": "14-апта: JSON есебін алу"
        }
    }


@app.get("/analyze")
def analyze():
    try:
        # Ортақ кодтар (9-апта)
        ci = CourseIntersection('enroll.csv', 'courses.csv')
        intersect = ci.get_intersection()

        # Топ курстар (12-апта)
        ca = CourseAnalytics('enroll.csv', 'courses.csv')
        top = ca.get_top_courses()

        return {
            "intersection_count": len(intersect),
            "common_codes": intersect,
            "top_course": top.iloc[0].to_dict() if not top.empty else "Мәлімет жоқ"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/chart")
def get_chart():
    """13-апта: График салып, оны сурет ретінде қайтарады"""
    if not os.path.exists('top_courses.csv'):
        # Егер файл жоқ болса, аналитиканы іске қосамыз
        ca = CourseAnalytics('enroll.csv', 'courses.csv')
        ca.get_top_courses()

    cv = CourseVisualizer('top_courses.csv')
    cv.draw_top_chart()
    return FileResponse("top_courses_chart.png", media_type="image/png")


@app.get("/report")
def get_report():
    """14-апта: Қорытынды JSON есебін қайтарады"""
    try:
        ca = CourseAnalytics('enroll.csv', 'courses.csv')
        top = ca.get_top_courses()

        # JSON форматына айналдыру
        report_data = top.to_dict(orient='records')

        # Файлға сақтау
        with open('final_report.json', 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)

        return JSONResponse(content=report_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)