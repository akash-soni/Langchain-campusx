from langchain_openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

# Initialize the LLM
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke the LLM
result = llm.invoke("What is the captital of India")

# Print the result
print(result)
