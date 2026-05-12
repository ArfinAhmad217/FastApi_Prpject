from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Conversation(Base):
    __tablename__ = "conversations"       # table ka naam

    id         = Column(Integer, primary_key=True)   # auto increment ID
    session_id = Column(String, nullable=False)       # konsi conversation
    role       = Column(String, nullable=False)       # "user" ya "assistant"
    content    = Column(Text, nullable=False)         # actual message
    created_at = Column(DateTime, default=datetime.utcnow)  # timestamp