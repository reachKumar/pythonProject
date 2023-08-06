import logging

file_path = "/py_temp/file_handling_message.txt"

logging.basicConfig(filename=file_path,
					format='%(asctime)s: %(levelname)s: %(message)s',
					level=logging.INFO)

try:
    fs = open (file_path,'x')
  
except:
    # setting logger to critical message
    logging.exception("File path exist")
   
finally:
    # setting logger to critical message
     logging.critical("This is a Critical Message!!!")
    





