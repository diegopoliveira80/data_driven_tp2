from pydantic import BaseModel


class Chatmodel(BaseModel):
    prompt: str