import pytest
from pages.homepage import HomePage
from pages.productpage import ProductPage
from tests.basetest import BaseTest

class TestSelenium(BaseTest):

#    def __init__(self, driver):
#        super().__init__(driver)

    @pytest.mark.smoke
    def test_open_samsung_galaxy_s6_page(self, driver):
        expected_samsung_galaxy_s6_title = "Samsung galaxy s6"
        homepage = HomePage(driver)
        homepage.open_homegape()
        homepage.click_first_product_page_link()
        samsung_galaxy_s6 = ProductPage(driver)
        #using assertion directly in test
        assert samsung_galaxy_s6.check_found_product_title() == expected_samsung_galaxy_s6_title
        #or comment out previus line and use indirect assertions in custom methods outside test
        #samsung_galaxy_s6.check_given_product_title(expected_samsung_galaxy_s6_title)
    
    @pytest.mark.regression
    def test_count_monitors_products(self, driver):
        expected_count = 2
        homepage = HomePage(driver)
        homepage.open_homegape()
        homepage.click_monitors_categorylink()
        #using assertion directly in test
        assert homepage.count_found_monitors(delay=10) == expected_count
        #or comment out previus line and use indirect assertions in custom methods outside test
        #homepage.count_given_monitors(expected_count, delay=5)
 
