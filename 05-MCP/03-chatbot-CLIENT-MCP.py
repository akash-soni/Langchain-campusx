from langgraph.graph import StateGraph, START
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_core.tools import tool
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import traceback
import os
import sys

load_dotenv()   

llm = ChatOpenAI(model="gpt-5")


CLIENT = MultiServerMCPClient(
    {
    #Local server example
    "Math": {
        "transport": "stdio",
        "command": "python",
         "args":[r"C:\\learning\\gen_ai\\campusx\\MCP-MATH-SERVER\\main.py" ],
    },
    # "expense": {
    #     "transport": "sse",
    #      "url": "https://rising-apricot-earwig.fastmcp.app/mcp"
    # },
}

)


#states
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

async def build_graph():

    try:
        tools = await CLIENT.get_tools()
        print("Loaded tools:", tools)
    except Exception:
        print("Error while loading MCP tools:")
        traceback.print_exc()
        print("Current Python executable:", sys.executable)
        print("Working directory:", os.getcwd())
        print("Environment PATH (tail):", os.environ.get("PATH", "")[-200:])
        raise

    llm_with_tools = llm.bind_tools(tools)


    # nodes
    async def chat_node(state: ChatState) :

        messages = state["messages"]
        response = await llm_with_tools.ainvoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools) # this is asynchronous by default
    # defining graphs and nodes
    graph = StateGraph(ChatState)


    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)


    # defining graphs connections
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    chatbot = graph.compile()

    return chatbot


async def main():
    
    chatbot = await build_graph()
    # running the graph
    result = await chatbot.ainvoke({"messages": [HumanMessage(content="What is 12 multiplied by 15? and reply as a cricket commentator")
                                        ]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())