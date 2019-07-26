import logging

logging.basicConfig(filename="C:\\Users\\aahme\\Desktop\\logfiles\\test.log",
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I/%M/%S %p') #What level do we debug here

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("MESSAGE GOES HERE")   