# https://www.amazon.com/
# C:\Users\mahadev_budake\Downloads\chromedriver_win32\chromedriver.exe
# //div//input[@id='twotabsearchtextbox']
# //span//input[@class='a-button-input' and @data-action-type='DISMISS']

import pytest
import allure

from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_CheckOut:

    def test_amazon(self):

        self.driver = webdriver.Chrome()

        self.driver.get("https://www.amazon.com/")

        self.driver.maximize_window()

        delay = 10  # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(
                (By.XPATH, "//span//input[@class='a-button-input' and @data-action-type='DISMISS']"))).click()
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")

        myElem = WebDriverWait(self.driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//div//input[@id='twotabsearchtextbox']")))

        # inputElement = driver.find_element("XPATH","//div//input[@id='twotabsearchtextbox']")
        myElem.send_keys('tv')
        myElem.submit()

        delay = 10  # seconds

        Title = self.driver.title

        print(Title)

        if Title == "Amazon.com : tv":
            assert True
        else:
            assert False

        delay = 5  # seconds

        print(self.driver.current_url)

        self.driver.get_screenshot_as_file("C://Users//mahadev_budake//Downloads//Screenshots//image.png")

        # myElemNext = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//title")))

        delay = 10  # seconds

        myElemRating = WebDriverWait(self.driver, delay).until(
            EC.presence_of_element_located((By.XPATH, "//section[@aria-label='4 Stars & Up']"))).click()

        delay = 10  # seconds

        myElemBrands = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located(
            (By.XPATH, "//li[@id='p_89/SAMSUNG']/span/a/div/label/i[@class='a-icon a-icon-checkbox']"))).click()

        delay = 10  # seconds

        # myElemProductClick = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//a//span[text()='SAMSUNG 32-inch Class LED Smart FHD TV 1080P (UN32N5300AFXZA, 2018 Model), Black']"))).click()

        myElement = self.driver.find_element(By.XPATH,
                                        "//a//span[text()='SAMSUNG 32-inch Class LED Smart FHD TV 1080P (UN32N5300AFXZA, 2018 Model), Black']").click()

        delay = 10  # seconds

        myElementAddtoCart = self.driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']").click()

        delay = 10  # seconds

        myElementCheckout = self.driver.find_element(By.XPATH, "//input[@name='proceedToRetailCheckout']").click()

        delay = 10  # seconds

        # input("Press ENTER to exit\n")

        # driver.close()
