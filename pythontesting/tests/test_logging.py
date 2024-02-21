import logging
logger =logging.getLogger(__name__)

logger.debug("this is a debug message")
logger.info("this is info msg")
logger.warning("this is warning msg")
logger.error("error msg this is")
logger.critical("critical msg this is")

filehandler=logging.FileHandler("logfile.log")
logger.addHandler(filehandler)
#add formatter and connect formatter with file handler
formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
filehandler.setFormatter(formatter)





