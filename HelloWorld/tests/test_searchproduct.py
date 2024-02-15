#https://www.amazon.com/
#C:\Users\mahadev_budake\Downloads\chromedriver_win32\chromedriver.exe
#//div//input[@id='twotabsearchtextbox']
#//span//input[@class='a-button-input' and @data-action-type='DISMISS']
import time
import calendar
from HelloWorld.Excel_Read_and_Write import excelReadWrite
from HelloWorld.Excel_Read_and_Write import getCurrentTime
from HelloWorld.Home_page import Locators
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_SearchProduct(Base_Test):

    def test_searchProduct(self):
        #driver = webdriver.Chrome()

        self.driver.get("https://www.amazon.com/")

        self.driver.maximize_window()

        delay = 10 # seconds
        getLocators = Locators.HomePageLocators()
        try:
            #getLocators = Locators.HomePageLocators()
            print(getLocators.getproductsearchtext())
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, getLocators.getproductsearchtext()))).click()
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, getLocators.getproductsearch())))

        #inputElement = driver.find_element("XPATH","//div//input[@id='twotabsearchtextbox']")

        #print(excelReadWrite.ExcelReadWrite.OpenandReadExcel(self))
        myElem.send_keys(excelReadWrite.ExcelReadWrite.OpenandReadExcel(self))
        myElem.submit()

        delay = 10 # seconds

        Title = self.driver.title

        print("Printed Title: "+Title)

        assert Title == "Amazon.com : table"

        delay = 5 # seconds

        print(self.driver.current_url)

        getCurrentTimeObj = getCurrentTime.GetCurrentTime()

        print(getCurrentTimeObj.getcurrenttime())

        self.driver.get_screenshot_as_file("C://Users//mahadev_budake//Downloads//Screenshots//image"+getCurrentTimeObj.getcurrenttime()+".png")

        #input("Press ENTER to exit\n")

        #driver.close()
