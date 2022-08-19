from typing import Union, Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantidade: str
    valor: float

app = FastAPI()

banco_de_dados = []

@app.get("/")
def read_root(user_agent: Optional[str] = Header (None)):
    return {"user_agent": user_agent}

@app.post("/item")
def add_item(item: Item):
    banco_de_dados.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in banco_de_dados:
        if item_id == item.id:
            return {"id": item.id, "quandidade ": item.quantidade, "valor": item.valor}

@app.get("/item/valor_total")
def get_valor_total(): 
	valor_total = 0.0
	for item in banco_de_dados:
		valor_total+=item.valor*item.quantidade
	return valor_total
