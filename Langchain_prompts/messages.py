# Step 1: Import Required Libraries
# - SystemMessage, HumanMessage, AIMessage: For creating structured chat messages
# - ChatOpenAI: For using OpenAI's chat models
# - dotenv: For managing environment variables
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai  import ChatOpenAI
from dotenv import load_dotenv

# Step 2: Environment Setup
# Load API keys and other environment variables from .env file
load_dotenv()

# Step 3: Model Initialization
# Create an instance of ChatOpenAI with default parameters
model = ChatOpenAI()

# Step 4: Create Message Sequence
# Initialize a list of messages containing:
# - A system message that defines the AI's role
# - A human message asking about Langchain
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content = "Tell me about Langchain")
]

# Step 5: Generate Response
# Use the model to generate a response based on the message sequence
result = model.invoke(messages)

# Step 6: Update Message History
# Add the AI's response to the message sequence
messages.append(AIMessage(content=result.content))

# Step 7: Display Results
# Print the complete message sequence including:
# - System message
# - Human message
# - AI's response
print(messages)