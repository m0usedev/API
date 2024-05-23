import os

def file_exists(file_path):
	"""
	Verifica si un archivo existe en un directorio.

	Args:
	- directory (str): El directorio donde buscar el archivo.
	- filename (str): El nombre del archivo a buscar.

	Returns:
	- bool: True si el archivo existe, False en caso contrario.
	"""
	# Comprueba si el archivo existe en el directorio
	file_path = os.path.join(file_path)
	return os.path.exists(file_path)

def file_delete(file_path):
  try:
    os.remove(file_path)
    return True
  except Exception as e:
    return False
