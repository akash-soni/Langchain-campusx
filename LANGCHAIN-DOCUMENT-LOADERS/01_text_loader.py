from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('LANGCHAIN-DOCUMENT-LOADERS\cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)