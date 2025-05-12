# Import required libraries
from langchain_openai import ChatOpenAI  # For using OpenAI's chat models
import streamlit as st  # For creating the web interface
from dotenv import load_dotenv  # For loading environment variables
from langchain_core.prompts import PromptTemplate, load_prompt  # For creating and managing prompts

# Load environment variables from .env file
load_dotenv()

# Initialize the ChatOpenAI model with default parameters
model = ChatOpenAI()

# Create the Streamlit web interface header
st.header('Research Tool')

# Create dropdown selectors for user input
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# Define the prompt template with placeholders for dynamic content
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}  
        Explanation Length: {length_input}  
        1. Mathematical Details:  
              - Include relevant mathematical equations if present in the paper.  
              - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
        2. Analogies:  
              - Use relatable analogies to simplify complex ideas.  
        If certain information is not available in the paper, respond with: 
        "Insufficient information available" instead of guessing.  
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""
)

# Define the variables that will be used to fill the template
input_variables = ['paper_input','style_input','length_input']

# Fill the template with user-selected values
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

# Create a button to trigger the summarization
if st.button('Summarize'):
    # Generate the summary using the model
    result = model.invoke(prompt)
    # Display the generated summary
    st.write(result.content)

