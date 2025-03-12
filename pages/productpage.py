from selenium.webdriver.common.by import By

class ProductPage:
    
    def __init__(self, driver):
        self.driver = driver

    def check_product_title(self, title):
        product_page = self.driver.find_element(By.CSS_SELECTOR, 'h2.name')
        product_title = product_page.text
        assert product_title == title
        #return product_title 