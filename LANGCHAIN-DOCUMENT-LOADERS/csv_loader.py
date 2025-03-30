from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(template='Write a summary for the data - using the given data \n{data}', input_variables=['data'])

parser = StrOutputParser()

loader = CSVLoader(file_path='LANGCHAIN-DOCUMENT-LOADERS\Social_Network_Ads.csv')

docs = loader.load()


chain = prompt | model | parser

print(len(docs))
print(docs[1])

print('SUMMARY\n')
print(chain.invoke({'data': docs}))