import selenium
class BasePage():
    
    def __init__(self, driver, url: str = None):
        self.driver = driver
        self.url = url
    
    def open(self):
        self.driver.get(self.url)
    
    def find_element(self, args):
        return self.driver.find_element(*args)

    def find_elements(self, args):
        return self.driver.find_elements(*args) 