from pydantic import BaseModel

class EntryBase(BaseModel):
    title: str
    content: str

class EntryCreate(EntryBase):
    pass

class Entry(EntryBase):
    id: int

    class Config:
        orm_mode = True
