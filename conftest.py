from typing import Any, Generator
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

@pytest.fixture(name="obj_id")
def fixture_obj_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
        }
    }
    print("Creating new product")
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    response_json = response.json()
    yield response_json["id"]
    requests.delete(f'https://api.restful-api.dev/objects/{response_json["id"]}')

@pytest.fixture(name="driver")
def fixture_driver() -> Generator[WebDriver, Any, None]:
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit() 

@pytest.fixture(scope='function', name="before_after")
def fixture_before_after():
    print("Fixture before running test")
    yield
    print("Fixture after running test")