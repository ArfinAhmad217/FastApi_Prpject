from fastapi import FastAPI
from pydantic import BaseModel
from ai_service import ask_ai

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "API is running and fetch the data from LLM 🚀"}

@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}


@app.post("/ask")
async def ask(body: QuestionRequest):
    answer = ask_ai(body.question)
    return {"answer": answer}