# Step 1: Import necessary libraries
# - ChatOpenAI: For using OpenAI's language models
# - streamlit: For creating the web interface
# - dotenv: For managing environment variables
# - PromptTemplate: For handling prompt templates
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

# Step 2: Environment Setup
# Load environment variables from .env file for API keys
load_dotenv()

# Step 3: Model Initialization
# Create an instance of ChatOpenAI with default settings
model = ChatOpenAI()

# Step 4: Create Streamlit UI
# Add a header to the web interface
st.header('Research Tool')

# Step 5: Create User Input Components
# Create dropdown menus for user to select:
# - Research paper to summarize
# - Desired explanation style
# - Preferred length of summary
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Step 6: Load Prompt Template
# Load the prompt template from an external JSON file
# This separates the prompt structure from the code
template = load_prompt('Langchain_prompts/template.json')

# Step 7: Define Template Variables
# List of variables that will be replaced in the template
input_variables = ['paper_input','style_input','length_input']

# Step 8: Process User Input
# Fill the template with user-selected values
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

# Step 9: Generate and Display Summary
# When user clicks the button:
# 1. Generate summary using the model
# 2. Display the result in the web interface
if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)

