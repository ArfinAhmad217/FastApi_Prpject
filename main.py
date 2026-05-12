from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, Conversation
from pydantic import BaseModel
from ai_service import ask_ai

# Tables auto-create
Base.metadata.create_all(bind=engine)

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    session_id: str       

@app.get("/")
def home():
    return {"message": "API is running and fetch the data from LLM 🚀"}

# @app.get("/user/{id}")
# def get_user(id: int):
#     return {"id": id}


@app.post("/ask")
async def ask(body: QuestionRequest, db: Session = Depends(get_db)):

 # Step 1 — DB se history fetch karo
    history_rows = db.query(Conversation)\
                     .filter(Conversation.session_id == body.session_id)\
                     .order_by(Conversation.created_at)\
                     .all()


# Step 2 — LLM format mein convert karo
    history = [{"role": row.role, "content": row.content} for row in history_rows]


# Step 3 — AI ko bhejo (history ke saath)
    answer = ask_ai(body.question, history)

     # Step 4 — User message save karo
    db.add(Conversation(
        session_id=body.session_id,
        role="user",
        content=body.question
    ))


 # Step 5 — AI response save karo
    db.add(Conversation(
        session_id=body.session_id,
        role="assistant",
        content=answer
    ))

    db.commit()

    return {"answer": answer, "session_id": body.session_id}
  
@app.get("/history/{session_id}")
def get_history(session_id: str, db: Session = Depends(get_db)):
    rows = db.query(Conversation)\
             .filter(Conversation.session_id == session_id)\
             .order_by(Conversation.created_at)\
             .all()
    return rows