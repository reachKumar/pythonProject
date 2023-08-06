import logging
import os

file_path = "/py_temp/"
full_file_path = file_path + "file_handling_message.txt"

logging.basicConfig(filename=full_file_path,
					format='%(asctime)s: %(levelname)s: %(message)s',
					level=logging.INFO)

#current_dir = os.getcwd()
#print(current_dir)

try:
    fs = open (full_file_path,'a')
    #os.rename(full_file_path,current_dir+"/"+"New.txt")
  
except:
    # setting logger to critical message
    logging.exception("File path exist")
   
finally:
    # setting logger to critical message
     logging.critical("This is a Critical Message!!!")