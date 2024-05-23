from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import math
from fastapi.responses import FileResponse
from utilites.csv_profiling import generate_profiling
from utilites.files_func import file_exists
from utilites.const import DIRECTORY_CSV, DIRECTORY_PROFILING

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

@app.get( "/getfile/table/" )
async def root ( file : str, page : int = 1 ):
	ROW_PAGE_DIV = 25
	print(page)
	'''
 	page 1 - X no puede superar el maximo
  
  20 filas por pagina
  numero de filas entre 20 = numero de paginas
  
  json{
		tabla
	  numero de paginas maximo
	}
	'''
	filename = f"{file}.csv"
 
	file_path = f"{DIRECTORY_CSV}{filename}"

	if file_exists(file_path):
		df = pd.read_csv(DIRECTORY_CSV+filename)
  
		#obtener num paginas
		df_index = df.index.tolist()
		num_pages = math.ceil(len(df_index)/ROW_PAGE_DIV)
		# obtener filas correspondientes a pagina actial
  
		df_colums = df.columns.tolist()
		df_index_name = df.index.name if df.index.name else 'index'
	  
		df_json = {
			'table' : {},
			'num_pages' : num_pages
		}

		# df_json['table'][df_index_name] = df_index
		for c in df_colums:
			df_json['table'][c] = df[c].to_list()

		return df_json
  
	return { "error" : 'file not found' }

@app.get( "/getfile/profile/")
async def root ( file : str):
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