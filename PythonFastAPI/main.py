from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/entries", response_model=list[schemas.Entry])
def get_entries(db: Session = Depends(get_db)):
    return db.query(models.JournalEntry).all()

@app.get("/entries/{id}", response_model=schemas.Entry)
def get_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

@app.post("/entries", response_model=schemas.Entry)
def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    db_entry = models.JournalEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.put("/entries/{id}", response_model=schemas.Entry)
def update_entry(id: int, entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db_entry.title = entry.title
    db_entry.content = entry.content
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.delete("/entries/{id}")
def delete_entry(id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == id).first()
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(db_entry)
    db.commit()
    return {"message": "Entry deleted"}
