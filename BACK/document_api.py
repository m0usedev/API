from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Objeto con el que manejaremos la API

# Primero haz: cd .\BACK\
# uvicorn document_api:app --reload

class Item(BaseModel):
	name: str

@app.get( "/get/" )
async def root ( text : str ) -> dict:
	return { "text" : text }


@app.post( "/post/" )
async def root ( item : Item ) -> dict:
	return { "item" : item.name }