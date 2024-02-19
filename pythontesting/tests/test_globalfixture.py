# def test_checkglobalworksornot1(test_global):
#     print("execute in file111")
#
# def test_checkglobalworksornot2(test_global):
#     print("execute in file222")
#
#
# def test_checkglobalworksornot3(test_global):
#     print("execute in file333")
#
#
# def test_checkglobalworksornot4(test_global):
#     print("execute in file444")
import pytest


#now concept of class

@pytest.mark.usefixtures("test_global")
class Testexample:
    def test_checkglobalworksornot1(self):
        print("execute in file111")
    def test_checkglobalworksornot2(self):
        print("execute in file222")
    def test_checkglobalworksornot3(self):
        print("execute in file333")
    def test_checkglobalworksornot4(self):
        print("execute in file444")