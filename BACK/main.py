from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import pandas as pd
from utilites.csv_profiling import generate_profiling
from utilites.files_func import file_exists, form_file_path, file_delete
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

# TEST
@app.get(
  path   			= "/test/get/",
  tags				= ["Test GET"],
  description = "**Path** a través del cual poder hacer una prueba de conexion **GET**"
)
async def funcPost ( text : str ):
	return { "text" : text }

@app.post(
  path   			= "/test/post/",
  tags				= ["Test POST"],
  description = "**Path** a través del cual poder hacer una prueba de conexion **POST**"
)
async def funcPost ( item : Item ):
	return { "item" : item.name }

# GET PROFILING
@app.get(
  path   				 = "/download/profile/",
  tags					 = ["Download Profile"],
  description    = "**Path** a través del cual subir obtener el **Profile** de las tablas **.csv** del servidor",
)
async def get_profile ( file_name : str ):
	try:
		fr = lambda fp : FileResponse(path=fp)
		fp_html = form_file_path(DIRECTORY_PROFILING, file_name, 'html')
		if(file_exists(fp_html)):
			return fr(fp_html)
		else :
			fp_csv = form_file_path(DIRECTORY_CSV, file_name, 'csv')
			if(file_exists(fp_csv)):
				df = pd.read_csv(fp_csv)
				generate_profiling(DIRECTORY_PROFILING, file_name, df)
				return fr(fp_html)
			else :
				return response('bad', 'El fichero csv necesaro que busca no existe en el servidor')
	except:
		return response('error', 'Ha surgido un error en el servidor')

# POST CSV
@app.post( 
	path   			= "/upload/csv/",
	tags				= ["Upload CSV"],
	description = "**Path** a través del cual subir al servidor tablas en formato **.csv**"
)
async def create_upload_file( file: UploadFile = File(...) ):
	try:
		if file.content_type != "text/csv" :
			return response('bad', 'El fichero fue subido al servidor no es tipo .csv')
	
		file_name = file.filename.split(".")[0]
		file_type = file.filename.split(".")[1]

		df = pd.read_csv(file.file, index_col=0)

		fp = form_file_path(DIRECTORY_CSV, file_name, file_type)
		df.to_csv(fp)
	
		fp = form_file_path(DIRECTORY_PROFILING, file_name, 'html')
		if(file_exists(fp)):
			file_delete(fp)
		return response('good', 'El fichero fue subido al servidor')
	except:
		return response('error', 'Ha surgido un error en el servidor')
	finally:
		file.close()
 
 
def response(type: str, message : str):
  return {
		"response" : type,
    "message"  : message
	}