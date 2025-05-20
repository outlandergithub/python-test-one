#from selenium.webdriver.common.by import By

from locators.productpage_locators import ProductPageLocators
from pages.basepage import BasePage

class ProductPage(BasePage):

    locators = ProductPageLocators()
    
    def __init__(self, driver, url: str = None):
        super().__init__(driver, url)
        #self.driver = driver
        if url == None:
            self.url = 'https://www.demoblaze.com/prod.html?idp_=1'

    def check_found_product_title(self):
        #TODO move locator to separate module class
        product_page = self.find_element(self.locators.PRODUCT_TITLE)
        actual_product_title = product_page.text
        #assert actual_product_title == title
        return actual_product_title 
    
    def check_given_product_title(self, title):
        #TODO move locator to separate module class
        product_page = self.find_element(self.locators.PRODUCT_TITLE)
        actual_product_title = product_page.text
        assert actual_product_title == title
        #return actual_product_title 

        