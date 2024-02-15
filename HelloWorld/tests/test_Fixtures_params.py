from selenium import webdriver
import pytest
#from HelloWorld import conftest

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_Google(Base_Test):
    def test_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"