from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3
import os

app = FastAPI()

class Input(BaseModel):
    user_id: str
    query: str

class Output(BaseModel):
    user_id: str
    query: str
    output: str

# データベースファイルのパス
DB_PATH = 'simple_database.db'


@app.post("/process/")
def main(input_data: Input):
    # 入力データを取得
    user_id = input_data.user_id
    query   = input_data.query


    # 文字列の加工処理
    processed_text = f"Processed_ User ID: {user_id}, Query: {query}"


    # データベースの存在を判定
    if os.path.exists(DB_PATH):
		# データベースが存在する場合
        print("attayo taburu ga arimashia")
        conn   = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
    else:
        # データベースが存在しない場合、新しく作成する
        print("nai table ga arimasen")
        conn   = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
	    
	    # テーブルの作成
        cursor.execute('''CREATE TABLE data
                      (USER_ID TEXT, QUERY TEXT, OUTPUT TEXT)''')

	# データの挿入
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)" ,(user_id, query, processed_text))

	# 変更を確定させる
    conn.commit()

	# データベース接続を閉じる
    conn.close()

    # 処理結果と入力データをまとめて返す
    output_data = Output(user_id=user_id, query=query, output=processed_text)
    return output_data