from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
app = FastAPI()

@app.put('/items{item_id}')
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {'item_id':item_id, **item.dict()}

    if q:
        result.update({'q':q})
    
    return result