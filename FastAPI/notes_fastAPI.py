'''
FastAPI для списка задач
Цель: Создать простое REST API с использованием FastAPI для управления списком задач.
реализовать базовые операции CRUD для списка задач. + пагинация - сделать ендпоинт в котороый передавать параметры для пагинации,
fastapi dev main.pyoffset - смещение от начала списка, limit - сколько элементов списка отображать

terminal check_point: fastapi dev notes_fastAPI.py

Serving at: http://127.0.0.1:8000

API docs: http://127.0.0.1:8000/docs
​'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime

app = FastAPI(
    title="Note App"
)

class Note(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: datetime
    #created_at: datetime.now()
    status: str

# Псевдо-база данных
notes_db: Dict[int, Note] = {
    1: Note(name="Python Homework", description="Complete FastAPI task", created_at=datetime.now(), status="in progress"),
    2: Note(name="Buy Groceries", description="Milk, eggs, bread", created_at=datetime.now(), status="new"),
    3: Note(name="Call John", description="Discuss project details", created_at=datetime.now(), status="active"),
    4: Note(name="Write Article", description="Finish writing article for blog", created_at=datetime.now(), status="in progress"),
    5: Note(name="Walk the Dog", description="Take the dog for a 30-minute walk", created_at=datetime.now(), status="new"),
}

@app.get("/notes/", response_model=List[Note])
async def get_notes(skip: int = 0, limit: int = 7):
    return list(notes_db.values())[skip: skip + limit]

'''
@app.post("/notes/", response_model=Note, status_code=201)
async def create_note(note: Note):
    note_id = max(notes_db.keys(), default=0) + 1
    notes_db[note_id] = note
    return note
'''
# or variant 
@app.post("/notes/", response_model=Note, status_code=201)
async def create_note(note: Note):
    note_id = max(notes_db.keys(), default=0) + 1
    note.created_at = datetime.now()  # Устанавливаем текущее время при создании заметки
    notes_db[note_id] = note
    return note

@app.get("/notes/{note_id}", response_model=Note)
async def get_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes_db[note_id]

@app.put("/notes/{note_id}", response_model=Note)
async def update_note(note_id: int, updated_note: Note):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    notes_db[note_id] = updated_note
    return updated_note

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes_db[note_id]
    return {"message": "Note deleted successfully"}
