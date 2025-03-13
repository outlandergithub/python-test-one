from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from pages.basepage import BasePage

class HomePage(BasePage):

    locator_first_product_page_link = (By.CSS_SELECTOR, 'h4 a.hrefch[href*="prod.html?idp_="]')
    locator_monitors_categorylink = (By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
    locator_first_phone_product_page_link = (By.CSS_SELECTOR, 'h4 a.hrefch[href="prod.html?idp_=1"]')
    locator_product_item_link = (By.CLASS_NAME, 'card')

    def __init__(self, driver, url: str = None):
        super().__init__(driver, url)
        #self.driver = driver
        if url == None:
            #TODO move hardcoded value to .env
            self.url = 'https://www.demoblaze.com/'

    def open_homegape(self):
        #TODO move hardcoded value to .env
        #base_url = 'https://www.demoblaze.com/'
        #self.driver.get(self.url)
        self.open()

    def click_first_product_page_link(self):
        #TODO move locator to separate module class
        links = self.find_elements(self.locator_first_product_page_link)
        links[0].click()
        #link = self.driver.find_elements(By.CSS_SELECTOR, 'h4 a.hrefch[href*="prod.html?idp_="]')
        #link[0].click()

    def click_monitors_categorylink(self):
        #TODO move locator to separate module class
        #link = self.driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
        #link.click()
        menu_link = self.find_element(self.locator_monitors_categorylink)
        menu_link.click()

    def count_found_monitors(self):
        delay = 1
        #TODO move locators to separate module class
        try:
            WebDriverWait(self.driver, timeout=delay).until(expected_conditions.invisibility_of_element_located(self.locator_first_phone_product_page_link))
            wait_more = WebDriverWait(self.driver, timeout=delay)
            products = wait_more.until(expected_conditions.visibility_of_all_elements_located(self.locator_product_item_link))
            actual_products_count = len(products)
        except TimeoutException:
            print("Elements were not found!\n"
                  "Something went wront - either loading the page was too low, or locator is no longer correct.\n")
            return 0
        return actual_products_count
    
    def count_given_monitors(self, count):
        delay = 1
        #TODO move locators to separate module class
        try:
            WebDriverWait(self.driver, timeout=delay).until(expected_conditions.invisibility_of_element_located(self.locator_first_phone_product_page_link))
            wait_more = WebDriverWait(self.driver, timeout=delay)
            products = wait_more.until(expected_conditions.visibility_of_all_elements_located(self.locator_product_item_link))
            actual_products_count = len(products)
        except TimeoutException:
            print("Elements were not found!\n"
                  "Something went wront - either loading the page was too low, or locator is no longer correct.\n")
            return 0
        assert actual_products_count == count
        #return actual_products_count
