import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['OPENAI_API_KEY']
print('myAPIkey='+api_key)

llm=OpenAI(model_name="text-davinci-003",openai_api_key=api_key)
#openAIインスタンスを作るときはopenai_api_key変数にAPIキーを渡す必要あり
print("ハロー？")
response=llm("教育学的な視点から教育をすることの意義を説明する")
print(response.score)