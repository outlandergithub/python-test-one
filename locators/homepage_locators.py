from selenium.webdriver.common.by import By

class HomePageLocators():
    
    FIRST_PRODUCT_PAGE_LINK = (By.CSS_SELECTOR, 'h4 a.hrefch[href*="prod.html?idp_="]')
    MONITORS_CATEGORY_LINK = (By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
    FIRST_PHONE_PRODUCT_PAGE_LINK = (By.CSS_SELECTOR, 'h4 a.hrefch[href="prod.html?idp_=1"]')
    PRODUCT_ITEM_LINK = (By.CLASS_NAME, 'card')
