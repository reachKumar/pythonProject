import logging

# configuring the logger to display log message
# along with log level and time
error_file_path= "/py_temp/error_msg.log"
logging.basicConfig(filename=error_file_path,
					format='%(asctime)s: %(levelname)s: %(message)s',
					level=logging.INFO)

# setting logger to critical message
logging.critical("This is a Critical Message!!!")
