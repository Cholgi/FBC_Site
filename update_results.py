import json
import os

# ▶ 1. 입력 데이터
title = "네 번째 뉴스입니다."
image_path = "images/news4.jpg"

# ▶ 2. JSON 파일 경로
json_path = "web/data/news_results.json"
os.makedirs(os.path.dirname(json_path), exist_ok=True)

# ▶ 3. 기존 데이터 불러오기
news_data = []
if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content:  # 파일이 비어있지 않으면
            news_data = json.loads(content)

# ▶ 4. ID 생성
new_id = f"news{len(news_data) + 1}"

# ▶ 5. 새 항목 추가
new_entry = {
    "id": new_id,
    "title": title,
    "image": image_path
}
news_data.append(new_entry)

# ▶ 6. JSON 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=2)

# ▶ 7. Git에 반영
os.system(f"git add {json_path}")
os.system(f'git commit -m "Add news: {new_id}"')
os.system("git push origin main")
