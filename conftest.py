import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    #options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close() 

@pytest.fixture
def obj_id():
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
    requests.delete(f'https://api.restful-api.dev/objects/{response_json["id"]}', json=payload)

@pytest.fixture(scope='function')
def before_after():
    print("Fixture before running test")
    yield
    print("Fixture after running test")