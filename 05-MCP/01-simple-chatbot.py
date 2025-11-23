from langgraph.graph import StateGraph, START
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_core.tools import tool

load_dotenv()   

llm = ChatOpenAI(model="gpt-5")

@tool
def calculator(frist_number: float, second_number: float, operation: str) -> dict:
    """Performs a basic arithmetic operation on two numbers."""
    try:
        if operation == "add":
            return frist_number + second_number
        elif operation == "subtract":
            return frist_number - second_number
        elif operation == "multiply":
            return frist_number * second_number
        elif operation == "divide":
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            result = frist_number / second_number
        else:
            return {"error": f"Unsupported operation: {operation}"}
        
        return {"first_number": frist_number, "second_number": second_number, "operation": operation, "result": result
                }
    except Exception as e:
        return {"error": str(e)}
    

tools = [calculator]



llm_with_tools =  llm.bind_tools(tools)


#states

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# nodes
def chat_node(state: ChatState) :

    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)


# defining graphs and nodes
graph = StateGraph(ChatState)


graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)


# defining graphs connections
graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge("tools", "chat_node")

chatbot = graph.compile()

# running the graph
result = chatbot.invoke({"messages": [HumanMessage(content="What is 12 multiplied by 15? and reply as a cricket commentator")
                                      ]})

print(result["messages"][-1].content)