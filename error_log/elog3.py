import logging

# creating the logger object
logger = logging.getLogger()

# setting logger to a warning message
logger.warning('This is a Warning message!')

# configuring the logger to info log levek
logging.basicConfig(level=logging.INFO)

# setting the logger to a informative message
logging.info("This is an Informative message.")
