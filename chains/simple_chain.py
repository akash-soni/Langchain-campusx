# Step 1: Import Required Libraries
# - ChatOpenAI: For using OpenAI's chat models
# - dotenv: For managing environment variables
# - PromptTemplate: For creating structured prompts
# - StrOutputParser: For parsing model output as string
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Step 2: Environment Setup
# Load API keys and other environment variables from .env file
load_dotenv()

# Step 3: Create Prompt Template
# Define a template for generating facts about a topic
# The {topic} placeholder will be replaced with actual input
prompt = PromptTemplate(
    template='Generate 5 interesting facts about{topic}',
    input_variables=['topic']
)

# Step 4: Model Initialization
# Create an instance of ChatOpenAI with default parameters
model = ChatOpenAI()

# Step 5: Output Parser Setup
# Initialize a string output parser to format the model's response
parser = StrOutputParser()

# Step 6: Chain Creation
# Create a processing pipeline using the | operator:
# 1. prompt: Formats the input
# 2. model: Generates the response
# 3. parser: Formats the output
chain = prompt | model | parser

# Step 7: Execute Chain
# Run the chain with 'cricket' as the topic
result = chain.invoke({'topic':'cricket'})

# Step 8: Display Results
# Print the generated facts
print(result)

# Step 9: Visualize Chain
# Print an ASCII representation of the chain's structure
chain.get_graph().print_ascii()


