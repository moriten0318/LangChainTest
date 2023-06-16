from langchain.llms import OpenAI

llm=OpenAI(model_name="text-davinci-003")
llm("大阪市の人口について説明する")
print("HelloWorld")
