
from selenium.webdriver.common.by import By
import time

from pages.homepage import HomePage
from pages.productpage import ProductPage

def test_open_samsung_galaxy_s6_page(driver):
    homepage = HomePage(driver) 
    homepage.open_homegape()
    homepage.click_productpagelink()
    samsung_galaxy_s6 = ProductPage(driver)
    samsung_galaxy_s6.check_product_title("Samsung galaxy s6")
    # assert samsung_galaxy_s6.check_product_title == "Samsung galaxy s6"
    #assert driver.find_element(By.CSS_SELECTOR, 'h2.name').text == "Samsung galaxy s6"

def test_count_monitors_products(driver):
    #driver.get('https://www.demoblaze.com/')
    #link = driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
    #link.click()
    homepage = HomePage(driver)
    homepage.open_homegape()
    homepage.click_monitors_categorylink()
    time.sleep(2)
      #products = driver.find_elements(By.CSS_SELECTOR, '.card')
    #products = driver.find_elements(By.CLASS_NAME, 'card')
    assert homepage.count_monitors(2) == 2
