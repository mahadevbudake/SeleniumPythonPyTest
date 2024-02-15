#https://www.amazon.com/
#C:\Users\mahadev_budake\Downloads\chromedriver_win32\chromedriver.exe
#//div//input[@id='twotabsearchtextbox']
#//span//input[@class='a-button-input' and @data-action-type='DISMISS']
import time
import calendar
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HelloWorld.Excel_Read_and_Write import excelReadWrite
import pytest
@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_SelectFromDropDown (Base_Test):

    def test_SelectFromDD(self):

        #driver = webdriver.Chrome()

        self.driver.get("https://www.amazon.com/")

        self.driver.maximize_window()

        delay = 10 # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span//input[@class='a-button-input' and @data-action-type='DISMISS']"))).click()
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='nav-search-scope nav-sprite']"))).click()

        delay = 10 # seconds

        myElementCheckout = self.driver.find_element(By.XPATH, "//select[@aria-describedby='searchDropdownDescription']/option[text()='Automotive']").click()

        #input("Press ENTER to exit\n")

        #driver.close()
        delay = 10  # seconds
        excelReadWrite.ExcelReadWrite.OpenandWriteExcel(self)