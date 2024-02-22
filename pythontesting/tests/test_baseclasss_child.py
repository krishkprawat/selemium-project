from pythontesting.tests.BaseClass import BaseClass
class Testexample(BaseClass):
    def test_child_baseclass(self):
        log=self.test_loggingDemo()
        log.info()