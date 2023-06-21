import os
import platform

import openai
import chromadb
from dotenv import load_dotenv
from gpt_index import download_loader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

#PDFをLLMで読み込むテスト

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']
llm = ChatOpenAI(model_name="text-davinci-003",openai_api_key=api_key,temperature=TEMPERATURE)

summarize_prompt_template = """以下の文章を簡潔に要約してください。:
{text}
要約:"""

def _load_documents(self, file_path: str) -> list:
        CJKPDFReader = download_loader("CJKPDFReader")
        loader = CJKPDFReader(concat_pages=False)

        documents = loader.load_data(file=file_path)
        langchain_documents = [d.to_langchain_format() for d in documents]
        return langchain_documents

def _summarize(self, langchain_documents: list) -> str:
        summarize_template = PromptTemplate(
            template=summarize_prompt_template, input_variables=["text"])

        chain = load_summarize_chain(
            self.llm,
            chain_type="map_reduce",
            map_prompt=summarize_template,
            combine_prompt=summarize_template
        )

        summary = chain.run(langchain_documents)
        return summary
