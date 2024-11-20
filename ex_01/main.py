from fastapi import FastAPI
from .gpt2.routers.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router, prefix="/chat")