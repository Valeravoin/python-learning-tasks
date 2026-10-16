from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    tags = Column(Text, default=True)
    priority = Column(Integer, default=1)
    is_done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)