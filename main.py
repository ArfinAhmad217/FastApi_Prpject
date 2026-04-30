from fastapi import FastAPI, Query
from pydantic import BaseModel
from ai_service import ask_ai

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "API chal rahi hai 🚀"}

@app.get("/user/{id}")
def get_user(id: int):
    return {"id": id}


@app.post("/ask")
async def ask(body: QuestionRequest):
    answer = ask_ai(body.question)
    return {"answer": answer}