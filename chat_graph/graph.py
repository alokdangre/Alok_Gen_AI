from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_message
from langchain.chat_models import init_chat_model


class State(TypedDict): 
    messages: Annotated[list,add_messages]

llm = init_chat_model(model_provider="google", model = "gemini-4")

def chat_node(state: State):
    response = llm.invoke()