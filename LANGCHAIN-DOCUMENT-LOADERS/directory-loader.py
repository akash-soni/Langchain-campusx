from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

loader = DirectoryLoader(
    path='LANGCHAIN-DOCUMENT-LOADERS\\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()


""" 
in nutshell if the number of documents are very large then load() will result in longer 
load time and memory issue as everything has to be loaded at once, but in case of lazy_load()
it does not loads everything at once insted it generates a iterator with loads next object one by one

"""
#docs = loader.lazy_load()

print(len(docs))

print(docs[0].metadata)
print(docs[0].page_content)