
class HomePageLocators:
    def __init__(self):
        self.__ProductDropDown = "//span//input[@class='a-button-input' and @data-action-type='DISMISS']"
        self.__ProductSearch = "//div//input[@id='twotabsearchtextbox']"
        self.__ProductSearchText = "//span//input[@class='a-button-input' and @data-action-type='DISMISS']"

    def getproductsearchtext(self):
        print("Here")
        print(self.__ProductSearchText)
        return self.__ProductSearchText

    def getproductsearch(self):
        return self.__ProductSearch

    def getproductdropdown(self):
        return self.__ProductDropDown
