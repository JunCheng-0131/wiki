from flask_frozen import Freezer
from app import app  # 確保你的 Flask 實例名稱是 app

# 設定輸出的資料夾名稱為 docs (這是為了方便 GitHub Pages 讀取)
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("網站已冷凍完成！請查看 docs 資料夾。")