from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in/"
    )
    yield request_context
    request_context.dispose()

def test_api_post(api_request_context: APIRequestContext) -> None:
    data = {
    "name": "morpheus",
    "job": "leader"
    }
    new_record = api_request_context.post(
        f"/api/users", data=data
    )
    
    assert new_record.ok

    new_record_response = new_record.json()
    print("API test")
    print(f"variable: {new_record}")
    