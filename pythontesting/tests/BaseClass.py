import logging
class BaseClass:
    def test_loggingDemo(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.CRITICAL)
        return logger

#so basically i made a base class for our logger and this class can be used in any method in any file in any test cases.