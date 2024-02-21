import logging
def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is printed")
    logger.info("Information Messages this is ")
    logger.warning("Warning Messages this is")
    logger.error("this is Error Messages")
    logger.critical("this i skp Critical Issues")