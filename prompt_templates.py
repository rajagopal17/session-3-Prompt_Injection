import logging
import json
from datetime import datetime
import uuid
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage,BaseMessage
from langchain_core.exceptions import OutputParserException
from langchain_core.tools import tool
from dotenv import load_dotenv
import os
from typing import TypedDict, Annotated, Sequence
from operator import add
from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate




from typing import TypedDict, Annotated
import operator

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, END

load_dotenv()
#########################################
import re
from typing import TypedDict
from langgraph.graph import StateGraph, END
llm = ChatOpenAI(model="gpt-4.1-nano",temperature=0.7,api_key=os.getenv("OPENAI_API_KEY"))