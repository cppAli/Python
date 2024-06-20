from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Псевдо-база данных
items_db: Dict[int, Item] = {
    1: Item(name="Laptop", description="A personal computer for mobile use.", price=1000.0, tax=0.1),
    2: Item(name="Smartphone", description="A mobile phone with advanced features.", price=500.0, tax=0.08),
    3: Item(name="Tablet", description="A portable computer with a touchscreen.", price=300.0, tax=0.07),
    4: Item(name="Monitor", description="A display screen for computers.", price=150.0, tax=0.05),
    5: Item(name="Keyboard", description="An input device for typing.", price=50.0, tax=0.02),
    6: Item(name="Mouse", description="A pointing device for computers.", price=25.0, tax=0.02),
    7: Item(name="Printer", description="A device for printing documents.", price=200.0, tax=0.06),
    8: Item(name="Headphones", description="Audio device for personal listening.", price=80.0, tax=0.03),
    9: Item(name="Speakers", description="Audio output device for sound.", price=120.0, tax=0.04),
    10: Item(name="Webcam", description="A camera for video communication.", price=70.0, tax=0.03),
}

@app.get("/items/")
def get_items(limit: int = 1, offset: int = 0):
    items_list = list(items_db.values())
    return items_list[offset:offset + limit]

@app.post("/items/", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item_id] = item
    return items_db[item_id]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return items_db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}


