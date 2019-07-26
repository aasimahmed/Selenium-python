#Logging useful for traceability - DEBUG, INFO, WARNING, ERROR, CRITICAL normally we have to create a log file

import logging

logging.basicConfig(filename="C:\\Users\\aahme\\Desktop\\logfiles\\test.log",
                    format='%(asctime)s: %(levelname)s : %(message)s',
                    level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is a info message")

#We will see warning and above
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
