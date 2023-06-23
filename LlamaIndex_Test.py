import os
from dotenv import load_dotenv

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']

persist_dir = "./storage/"

documents = SimpleDirectoryReader("data").load_data()

for document in documents:
    print("data内のdocument =",document)