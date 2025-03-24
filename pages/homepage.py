from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from locators.homepage_locators import HomePageLocators
from pages.basepage import BasePage

class HomePage(BasePage):

    locators = HomePageLocators()

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
        links = self.find_elements(self.locators.FIRST_PRODUCT_PAGE_LINK)
        links[0].click()
        #link = self.driver.find_elements(By.CSS_SELECTOR, 'h4 a.hrefch[href*="prod.html?idp_="]')
        #link[0].click()

    def click_monitors_categorylink(self):
        #TODO move locator to separate module class
        #link = self.driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
        #link.click()
        menu_link = self.find_element(self.locators.MONITORS_CATEGORY_LINK)
        menu_link.click()

    def count_found_monitors(self):
        delay = 1
        #TODO move locators to separate module class
        try:
            WebDriverWait(self.driver, timeout=delay).until(expected_conditions.invisibility_of_element_located(self.locators.FIRST_PHONE_PRODUCT_PAGE_LINK))
            wait_more = WebDriverWait(self.driver, timeout=delay)
            products = wait_more.until(expected_conditions.visibility_of_all_elements_located(self.locators.PRODUCT_ITEM_LINK))
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
            WebDriverWait(self.driver, timeout=delay).until(expected_conditions.invisibility_of_element_located(self.locators.FIRST_PHONE_PRODUCT_PAGE_LINK))
            wait_more = WebDriverWait(self.driver, timeout=delay)
            products = wait_more.until(expected_conditions.visibility_of_all_elements_located(self.locators.PRODUCT_ITEM_LINK))
            actual_products_count = len(products)
        except TimeoutException:
            print("Elements were not found!\n"
                  "Something went wront - either loading the page was too low, or locator is no longer correct.\n")
            return 0
        assert actual_products_count == count
        #return actual_products_count
