from fastapi import APIRouter
from langchain_community.llms import FakeListLLM
from ..models.chat import Chatmodel


router = APIRouter()


def fake_list(prompt:str):
    fake_llm = FakeListLLM(responses = ["Done"])
    return fake_llm.invoke(prompt)
    

@router.post("/prompt/") # variavel = prompt
async def chat(body: Chatmodel):
    response = fake_list(body.prompt)
    return {"message": response}