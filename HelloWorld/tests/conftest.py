from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import pytest
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture(params=["chrome", "edge"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver = driver
    elif request.param == "edge":
        #driver = webdriver.Firefox()
        #binary = FirefoxBinary('C://Users//mahadev_budake//Downloads//Firefox.exe')
        driver = webdriver.Edge()
        request.cls.driver = driver
    request.cls.driver = driver
    yield
    driver.quit()