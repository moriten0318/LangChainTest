import os
import platform

import openai
from langchain import OpenAI
from dotenv import load_dotenv


#以下いらないかも
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

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

documents = loader.load_data("pdftest.pdf")#pdfからドキュメントを読み取る
index = GPTVectorStoreIndex.from_documents(documents)#indexの作成
index.storage_context.persist()#indexの保存


query_text ="本時のめあてを教えてください。"

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=350))
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
response = index.query(query_text, llm_predictor=llm_predictor)

print("Q:", query_text)
print("A:", str(response))