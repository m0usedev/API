from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI() # Objeto con el que manejaremos la API

# Primero haz: cd .\BACK\
# uvicorn main:app --reload

origins = [
  "http://localhost",
]

app.add_middleware( 
	CORSMiddleware, 
	allow_origins=origins, 
	allow_credentials=True, 
	allow_methods=["*"], 
	allow_headers=["*"],
  allow_origin_regex='http://localhost.*'
)

class Item(BaseModel):
	name: str

@app.get( "/get/{text}" )
async def root ( text : str ):
  return { "text" : text }

@app.get( "/getfile/" )
async def root ( file : str ):
	directory = "./FILES/"
	filename = f"{file}.csv"

	if file_exists(directory, filename):
		df = pd.read_csv(directory+filename, index_col=0)
  
		df_json = {
			'table' : {},
		}

		df_colums = df.columns.tolist()
		df_index_name = df.index.name if df.index.name else 'index'
  
		df_json['table'][df_index_name] = df.index.tolist()
		for c in df_colums:
			df_json['table'][c] = df[c].to_list()

		return df_json
  
	return { "error" : 'file not found' }

@app.post( "/post/" )
async def funcPost ( item : Item ):
	return { "item" : item.name }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
	file_content_type = file.content_type
 
	if file_content_type != "text/csv" :
		return { "error" : "no es del tipo esperado",}
 
	file_path = file.filename

	df = pd.read_csv(file.file, index_col=0)
 
	df.to_csv(f"./FILES/{file_path}")

	file.close()
	return {
    "file_content_type" : file_content_type,
    "file_path" : file_path
  }
 
 
def file_exists(directory, filename):
	"""
	Verifica si un archivo existe en un directorio.

	Args:
	- directory (str): El directorio donde buscar el archivo.
	- filename (str): El nombre del archivo a buscar.

	Returns:
	- bool: True si el archivo existe, False en caso contrario.
	"""
	# Comprueba si el archivo existe en el directorio
	file_path = os.path.join(directory, filename)
	return os.path.exists(file_path)