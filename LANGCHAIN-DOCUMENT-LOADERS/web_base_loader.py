from langchain_community.document_loaders import WebBaseLoader

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(template='Answer the following question  \n{question} from the following text - \n {text}', 
                        input_variables=['question','text'])

parser = StrOutputParser()

url = 'https://www.flipkart.com/kreo-ikarus-wireless-gaming-mouse-100-hours-battery-omron-optical-switches-mouse/p/itm1691a5179e797?pid=ACCH47WHE2YNWAJP&lid=LSTACCH47WHE2YNWAJPIYBLG1&marketplace=FLIPKART&sattr[]=color&st=color'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the warranty of this product?, Give is the summary of this product with recommendation to buy or not?', 'text':docs[0].page_content}))

# print(len(docs))

# print(docs[0].metadata)
# print(docs[0].page_content)