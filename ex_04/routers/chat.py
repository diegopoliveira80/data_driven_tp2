from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
from fastapi import APIRouter
from ..models.chat import Chatmodel


router = APIRouter()
load_dotenv()

def tradutor(text):
    template = ChatPromptTemplate([
        ("system", "You are an English to French translator."),
        ("user", "Tranlate this: {text}")
    ])
    
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    llm = ChatOpenAI(model = "gpt-4o-mini",
                     api_key=OPENAI_API_KEY)
    
    response = llm.invoke(template.format_messages(text=text))
    return response


@router.post("/ex_04/")
async def ex_04(body:Chatmodel):
    response = tradutor(body.text)
    return {"tradutor": response}