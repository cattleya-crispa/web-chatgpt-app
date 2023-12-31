import requests
import json
import os
import sqlite3
import pandas as pd


url = "http://localhost:8000/process/"  # POSTリクエストを送信するエンドポイントのURL

data = {
    "user_id": "example_user",
    "query"  : "example_query"
}

print("openai toiawase start")

response = requests.post(url, json=data)

# レスポンスの内容を表示
#print(response.json())

# ステータスコードを取得
status_code = response.status_code
print("status : " + str(status_code))


# データベースファイルのパス
DB_PATH = 'simple_database.db'

# データベースに接続
conn   = sqlite3.connect(DB_PATH)

# SQLクエリを実行し、データを取得
query = "SELECT * FROM data"
df    = pd.read_sql_query(query, conn)


# データベース接続を閉じる
conn.close()


# データフレームを表示
print(df)