from ydata_profiling import ProfileReport
from .files_func import file_exists, file_delete

def generate_profiling(file_name, d_profiling, df):
  profile = ProfileReport(df, title=file_name)
  file_path = f"{d_profiling}{file_name}.html"
  if(file_exists(file_path)) :
    file_delete(file_path)
  profile.to_file(f"{d_profiling}{file_name}.html")