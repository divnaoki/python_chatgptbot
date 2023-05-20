# -*- coding: utf-8 -*-

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# APIキーはいつか別ファイルで持たせる
api_key = os.getenv("CHATGPT_API_KEY")
openai.api_key = api_key

print(openai.api_key)
# チャットボットの初期化
def initialize_chat():
    print("チャットボット: こんにちは！何か質問してみてください")

# チャットのメインループ
def chat_loop():
    user_input = ""
    while user_input.lower() != "終了":
        user_input = input("ユーザー: ")
        response = generate_response(user_input)
        print("チャットボット:", response)

# ユーザーの入力に対して応答を生成する
def generate_response(user_input):
    prompt = "ユーザー: " + user_input + "\nチャットボット:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# メイン関数
def main():
    initialize_chat()
    chat_loop()

# プログラムの実行
if __name__ == "__main__":
    main()