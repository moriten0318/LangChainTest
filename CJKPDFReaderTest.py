import os

import openai
from langchain import OpenAI
from dotenv import load_dotenv


from llama_index import (
    GPTVectorStoreIndex,#Vector保存
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    download_loader,
)

#PDFをLLMで読み込むテスト
load_dotenv()
api_key = os.environ['OPENAI_API_KEY']
openai.api_key=api_key#APIキーを渡す

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()#PDF読み込みloader

documents = loader.load_data("data/testpdf.pdf")#pdfからドキュメントを読み取る
print(documents)