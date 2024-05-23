from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import math
from fastapi.responses import FileResponse
from utilites.csv_profiling import generate_profiling
from utilites.files_func import file_exists
from utilites.const import DIRECTORY_CSV, DIRECTORY_PROFILING

# Primero haz: cd .\BACK\
# uvicorn main:app --reload

app = FastAPI() # Objeto con el que manejaremos la API

# Direcciones permitidas
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

#Modelos de datos
class Item(BaseModel):
	name: str

# GET
@app.get( "/test/get/" )
async def funcPost ( text : str ):
	return { "text" : text }

@app.get( "/download/profile/")
async def get_profile ( file : str):
	'''
	1. Me llega el nombre de un file
	2. Busco el arhcivo profile.html de ese archivo
		2.1 Si no exise devolver False
		2.2 Si existe devolver True
	3. Si la respuesta es True 
	'''
	file_path = f"{DIRECTORY_PROFILING}{file}.html"
	if(file_exists(file_path)):
		return FileResponse(path=file_path)
	else :
		return {"error":"el fichero no existe"}

# POST
@app.post( "/test/post/" )
async def funcPost ( item : Item ):
	return { "item" : item.name }

@app.post("/upload/csv/")
async def create_upload_file(file: UploadFile = File(...)):
	file_content_type = file.content_type
 
	if file_content_type != "text/csv" :
		return { "error" : "no es del tipo esperado",}
 
	file_path = file.filename

	df = pd.read_csv(file.file, index_col=0)

	df.to_csv(f"{DIRECTORY_CSV}{file_path}")
 
	print(file_path.split(".")[0])
	print(DIRECTORY_PROFILING)
	print(df)
 
	generate_profiling(file_path.split(".")[0], DIRECTORY_PROFILING, df)

	file.close()

	return {
		"file_content_type" : file_content_type,
		"file_path" : file_path
	}