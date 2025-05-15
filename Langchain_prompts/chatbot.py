# Step 1: Import Required Libraries
# - ChatOpenAI: For using OpenAI's chat models
# - SystemMessage, HumanMessage, AIMessage: For structuring different types of chat messages
# - dotenv: For managing environment variables
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# Step 2: Environment Setup
# Load API keys and other environment variables from .env file
load_dotenv()

# Step 3: Model Initialization
# Create an instance of ChatOpenAI with default parameters
model = ChatOpenAI()

# Step 4: Initialize Chat History
# Create a list to store the conversation history
# Start with a system message that defines the AI's role
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

# Step 5: Main Chat Loop
# Continue the conversation until user types 'exit'
while True:
    # Get user input from the console
    user_input = input('You :')
    
    # Add user's message to chat history
    chat_history.append(HumanMessage(content=user_input))
    
    # Check for exit command
    if user_input == 'exit':
        break
    
    # Generate AI response using the entire chat history
    result = model.invoke(chat_history)
    
    # Add AI's response to chat history
    chat_history.append(AIMessage(content=result.content))
    
    # Display AI's response to the user
    print("AI: ", result.content)

# Step 6: End of Conversation
# Print the complete chat history when the conversation ends
print(chat_history)