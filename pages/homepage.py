from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

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
        delay = 1
        try:
            WebDriverWait(self.driver, timeout=delay).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, 'h4 a.hrefch[href="prod.html?idp_=1"]')))
            wait_more = WebDriverWait(self.driver, timeout=delay)
            products = wait_more.until(expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, 'card')))
            products_count = len(products)
        except TimeoutException:
            print("Surprise, ************\n"
                  "Something went wront - either loading the page was too low, or locator is no longer correct.\n"
                  "Therefore elements were not found!")
            return 0
        #assert products_count == count
        return products_count
    
    # count_monitors() function variant without WebDriverWait, but using sleep() commented function from test_selenium file
    #def count_monitors(self, count):
    #    products = self.driver.find_elements(By.CLASS_NAME, 'card')
    #    products_count = len(products)
    #    #assert products_count == count
    #    return products_count