from  __future__ import  print_function
import os

src_folder_path="c:/repo"
src_files_in= os.listdir(src_folder_path)
for src_file_nm in src_files_in:
  print(src_file_nm)