from sqlalchemy import Column, Integer, String, Text
from database import Base

class JournalEntry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
