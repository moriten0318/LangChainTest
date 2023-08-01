import os
import openai
from dotenv import load_dotenv
from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    download_loader,
)



persist_dir = "./LangChainTest/"#indexを作成する現在のディレクトリ
load_dotenv()
api_key = os.environ['OPENAI_API_KEY']
openai.api_key=api_key#APIキーを渡す

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()#PDF読み込みloader


def pdf_to_index(filename):#filename=("data/ファイル名")
    documents = loader.load_data(filename)#pdfからドキュメントを読み取る
    if not os.path.exists(persist_dir):
        os.mkdir(persist_dir)
    index = GPTVectorStoreIndex.from_documents(documents)#ドキュメントからindex作成
    index.storage_context.persist(persist_dir)#indexをpersist_dirディレクトリに保存
    return index

# load from disk

storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
# load index
index = load_index_from_storage(storage_context)

def print_response(prompt: str, index):
    query_engine = index.as_query_engine()
    print(query_engine.query(prompt))

print_response("教育学的視点からためになることを語ってください", index)