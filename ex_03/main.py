from fastapi import FastAPI
from .fake_llm.routers.chat import router as chat_router

app = FastAPI()


app.include_router(chat_router, prefix='/chat')

