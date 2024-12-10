from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# 1. 랜덤 여행지 데이터 생성
def generate_travel_destinations():
    destinations = [
        {"도시": "서울", "관광지": "경복궁"},
        {"도시": "부산", "관광지": "해운대"},
        {"도시": "제주", "관광지": "한라산"},
        {"도시": "강릉", "관광지": "경포대"},
        {"도시": "여수", "관광지": "오동도"},
        {"도시": "인천", "관광지": "월미도"},
        {"도시": "대전", "관광지": "대전엑스포"},
        {"도시": "수원", "관광지": "수원 화성"},
        {"도시": "전주", "관광지": "한옥마을"},
        {"도시": "안동", "관광지": "하회마을"}
    ]
    
    # 랜덤으로 여행지 5곳 추천
    selected_destinations = random.sample(destinations, 5)
    return selected_destinations


# 2. FastAPI 엔드포인트 작성
@app.get("/", response_class=HTMLResponse)
async def show_travel_destinations():
    destinations = generate_travel_destinations()
    
    # HTML 테이블로 변환
    table_html = """
    <table style="border-collapse: collapse; width: 60%; margin: 0 auto;">
        <tr>
            <th style="border: 1px solid #ddd; padding: 10px; text-align: center;">도시</th>
            <th style="border: 1px solid #ddd; padding: 10px; text-align: center;">관광지</th>
        </tr>
    """
    for destination in destinations:
        table_html += f"""
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{destination['도시']}</td>
            <td style="border: 1px solid #ddd; padding: 8px; text-align: center;">{destination['관광지']}</td>
        </tr>
        """
    
    table_html += "</table>"

    # HTML 콘텐츠
    html_content = f"""
    <html>
        <head>
            <title>랜덤 여행지 추천</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 20px;
                }}
                h1 {{
                    color: #555;
                }}
                table {{
                    margin: 20px auto;
                    border: 1px solid #ddd;
                    width: 80%;
                }}
                th, td {{
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: center;
                }}
                th {{
                    background-color: #f4f4f4;
                }}
            </style>
        </head>
        <body>
            <h1>🌏 랜덤 여행지 추천 시스템 🌏</h1>
            {table_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)