from numbers import Number
from operator import is_not
from typing import Dict, Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext, Page, expect

#FIXTURES
@pytest.fixture(name="clientam_request_context")
def fixture_clientam_request_context(playwright: Playwright, page):
    page.goto("https://www.clientam.com/sso/Login")
    browser_storage_state = page.context.storage_state(path="browser_storage_state.json",indexed_db=True)
    request_context = playwright.request.new_context(
        base_url="https://www.clientam.com",
        storage_state=browser_storage_state
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session", name="reqres_request_context")
def fixture_reqres_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in/",
        extra_http_headers = {"x-api-key": "reqres-free-v1"}
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session", name="page_request_context")
def fixture_page_request_context(playwright: Playwright):
        browser_context = playwright.chromium.launch(headless=False, slow_mo=500).new_context()
        page = browser_context.new_page()
        page.goto("https://gmail.com")
        print("Before yield --------")
        yield page
        print("\nBefore closing browsercontext --------")
        browser_context.close()
        print("\nAfter closing browsercontext --------")
        #print("\nBefore closing page --------")
        #page.wait_for_timeout(2000) # playwright._impl._errors.TargetClosedError: Page.wait_for_timeout: Target page, context or browser has been closed
        #page.close() # no error - still possible to call page.close() after its browser context has already been closed
        #print("After closing page --------")

#@pytest.fixture(scope="session")
#def page_request_context():
#    with sync_playwright() as p:
#        browser = p.chromium.launch(headless=False).new_context()
#        page = browser.new_page()
#        page.goto("https://i.ua")
#        print("Before yield --------")
#        yield page
#        page.close()

#HELPERES
def generate_pairs(): 
    pairs = []
    users = ["alan", "wake"]
    passwords = ["pass1", "pass2"]
    for user in users:
        for password in passwords:
            pairs.append(pytest.param((user,password), id=f"{user}, {password}"))
    return pairs

#TESTS
def test_api_add_user_post(reqres_request_context: APIRequestContext, page_request_context: Page) -> None:
    data = {
    "name": "morpheus",
    "job": "leader"
    }
    print(f"{page_request_context.title()} - page title printed here")
    print("\nBefore closing page --------")
    page_request_context.close()
    print("After closing page --------")
    new_record = reqres_request_context.post(
        f"/api/users", data=data
    )
    new_record_response_json = new_record.json()
    print("API test")
    print(f"variable: {new_record}")
    print(new_record_response_json["name"])
    assert new_record.ok
    assert new_record_response_json["name"] == data.get("name")
    assert new_record_response_json["job"] == data.get("job")

#PARAMETRIZED TESTS
@pytest.mark.parametrize("test_input,expected", 
                         [pytest.param("3+5", 8, id="3+5,8"), 
                          pytest.param("2+4", 6, id="2+4,6"), 
                          pytest.param("6*9",42, id="6*9,42", marks=pytest.mark.xfail)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.xfail
@pytest.mark.parametrize("credentials", generate_pairs())
def test_parametrized_generated_pairs(clientam_request_context: APIRequestContext, credentials):                            
    login, pas = credentials
    data = {
        "login": login,
        "password": pas
    }    
    response = clientam_request_context.post(
        url=f"/sso/Login", data=data)
    print(data)
    expect(response).to_be_ok()
    assert response.ok
    assert response.status == 200
    assert response.status_text == "OK"
    response_body = response.body()
    assert response_body is not None
    print(response.headers)
    #all following assertions fail, because a completely different response is returned to bare api request as opposed to same api request make in real browser
    #storage state is ignored also
    assert response.headers["content-type"] == "application/json;charset=ISO-8859-1" 
    response_json = response.json()
    assert response_json["user"] == "true"
    assert response_json["paper"] == "false"
    

#@pytest.mark.parametrize("name,job", [("morpheus1", "first"),("morpheus2", "second"), ("morpheus3", "")])
@pytest.mark.parametrize("name,job",
                         [("morpheus1", "proger"),
                          ("morpheus2", "tester"), 
                          pytest.param("morpheus3", "", marks=pytest.mark.xfail)])
def test_parametrized_api_add_user_post(reqres_request_context: APIRequestContext, name, job) -> None:
    data = {
    "name": name,
    "job": job
    }
    new_record = reqres_request_context.post(
        f"/api/users", data=data
    )
    new_record_response: Dict = new_record.json()
    print(new_record_response)
    assert new_record.ok
    print(new_record_response["name"])
    assert new_record_response["name"] == name
    print(new_record_response["job"])
    assert new_record_response["job"] == job
    #assert len(new_record_response["job"]) > 0, "Job title not given"
    #for key, value in new_record_response.items():
    #    print(key, value)
    #    print("---")
    #    assert value == name
    #    assert value is not None
    #for index,record in enumerate(new_record_response):
    #     print(index,record)
    j: int = 0
    for i in new_record_response.items():
         print(i)
         if j == 0:
            print(i[1])
            assert i[1] == name
            j += 1
            continue
         if j == 1:
            print(i[1])
            assert i[1] is not "", "Job title not given"
            assert i[1] == job
            break