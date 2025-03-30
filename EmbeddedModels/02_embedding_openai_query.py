from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]


embedding = OpenAIEmbeddings(model='text-embedding-3-large' ,dimensions=32)

result = embedding.embed_documents(documents)

print(str(result))