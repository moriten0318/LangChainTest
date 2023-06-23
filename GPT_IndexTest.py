import os
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']
openai_api_key=api_key

# インデックスの作成
documents = SimpleDirectoryReader('data').load_data()

for document in documents:
    print("data内のdocument =",document)

index = GPTSimpleVectorIndex(documents)

# 質問応答
print(index.query("禁止されたのはどのカードか？"))