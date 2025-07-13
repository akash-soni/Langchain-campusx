# Step 1: Import Dependencies
# - ChatOpenAI: For accessing OpenAI's language models
# - streamlit: For building the web interface
# - dotenv: For managing environment variables
# - PromptTemplate: For handling prompt templates
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

# Step 2: Environment Configuration
# Load API keys and other environment variables from .env file
load_dotenv()

# Step 3: Model Setup
# Initialize the ChatOpenAI model with default parameters
model = ChatOpenAI()

# Step 4: Create Web Interface
# Add a title to the Streamlit application
st.header('Research Tool')

# Step 5: Build User Input Components
# Create three dropdown selectors for:
# - Research paper selection
# - Explanation style preference
# - Desired summary length
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Step 6: Load Prompt Template
# Load the prompt structure from an external JSON file
# This separates the prompt logic from the application code
template = load_prompt('Langchain_prompts/template.json')

# Step 7: Define Template Variables
# List of variables that will be dynamically filled in the template
input_variables = ['paper_input','style_input','length_input']

# Step 8: Process User Request
# When the user clicks the Summarize button:
if st.button('Summarize'):
    # Create a processing chain by combining template and model
    # The | operator creates a pipeline where output of template becomes input to model
    chain = template | model
    
    # Execute the chain with user inputs
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    
    # Display the generated summary in the web interface
    st.write(result.content)

