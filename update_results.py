result = "테스트문구예용~"

import json
import os
os.makedirs("web/data", exist_ok=True)

with open("web/data/news_results.json", "a", encoding="utf-8") as f:
    f.write(result + "\n")  # 줄바꿈 포함해서 누적 저장


os.system("git add web/data/news_results.json")
os.system('git commit -m "update result"')
os.system("git push origin main")  # 브랜치 이름에 따라 'main' or 'master'

