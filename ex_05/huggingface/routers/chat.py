from fastapi import APIRouter
from ..models.chat import ChatModel
from transformers import pipeline

router = APIRouter()


def generate_response(message: str):
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
    return pipe(message)


@router.post("/tradutor/")
async def chat(body: ChatModel):
    response = generate_response(body.tradutor)
    return {"tradutor": response}