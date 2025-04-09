import pytest
from pages.homepage import HomePage
from pages.productpage import ProductPage
#from tests.basetest import BaseTest
from tests.basetest import BaseTest

#class TestSelenium():
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
        #samsung_galaxy_s6.check_given_product_title(expected_samsung_galaxy_s6_title)
        assert samsung_galaxy_s6.check_found_product_title() == expected_samsung_galaxy_s6_title

    @pytest.mark.regression
    def test_count_monitors_products(self, driver):
        expected_count = 2
        homepage = HomePage(driver)
        homepage.open_homegape()
        homepage.click_monitors_categorylink()
        #homepage.count_given_monitors(expected_count, delay=5)
        assert homepage.count_found_monitors(delay=5) == expected_count

 
