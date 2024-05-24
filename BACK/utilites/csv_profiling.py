from pandas import DataFrame
from ydata_profiling import ProfileReport
from .files_func import file_exists, file_delete, form_file_path

def generate_profiling(d_profiling : str, file_name : str, df : DataFrame):
  profile = ProfileReport(df, title=file_name)
  fp =  form_file_path(d_profiling, file_name, 'html')
  profile.to_file(fp)
  