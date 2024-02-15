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

class Test_SearchProduct:

    def test_searchProduct(self):
        driver = webdriver.Chrome()

        driver.get("https://www.amazon.com/")

        driver.maximize_window()

        delay = 10 # seconds
        getLocators = Locators.HomePageLocators()
        try:
            #getLocators = Locators.HomePageLocators()
            print(getLocators.getproductsearchtext())
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, getLocators.getproductsearchtext()))).click()
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, getLocators.getproductsearch())))

        #inputElement = driver.find_element("XPATH","//div//input[@id='twotabsearchtextbox']")

        #print(excelReadWrite.ExcelReadWrite.OpenandReadExcel(self))
        myElem.send_keys(excelReadWrite.ExcelReadWrite.OpenandReadExcel(self))
        myElem.submit()

        delay = 10 # seconds

        Title = driver.title

        print("Printed Title: "+Title)

        assert Title == "Amazon.com : table"

        delay = 5 # seconds

        print(driver.current_url)

        getCurrentTimeObj = getCurrentTime.GetCurrentTime()

        print(getCurrentTimeObj.getcurrenttime())

        driver.get_screenshot_as_file("C://Users//mahadev_budake//Downloads//Screenshots//image"+getCurrentTimeObj.getcurrenttime()+".png")

        #input("Press ENTER to exit\n")

        #driver.close()
