from fastapi import APIRouter
from ..models.chat import ChatModel
from transformers import pipeline

router = APIRouter()


def generate_response(message: str):
    generator = pipeline('text-generation', model='gpt2')
    return generator(message)


@router.post("/message/")
async def chat(body: ChatModel):
    response = generate_response(body.message)
    return {"assistant": response}