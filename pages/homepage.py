from selenium.webdriver.common.by import By
from selenium import *

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_homegape(self):
        self.driver.get('https://www.demoblaze.com/') 

    def click_productpagelink(self):
        link = self.driver.find_elements(By.CSS_SELECTOR, 'h4 a.hrefch[href*="prod.html?idp_="]')
        link[0].click()

    def click_monitors_categorylink(self):
        link = self.driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
        link.click()

    def count_monitors(self, count):
        products = self.driver.find_elements(By.CLASS_NAME, 'card')
        products_count = len(products)
        #assert products_count == count
        return products_count