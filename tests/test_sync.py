
import pytest
from playwright.sync_api import sync_playwright, BrowserContext, APIRequestContext, APIResponse

# test that finishes successfully if run from file/module or by its name, but fails if run with pytest without specifying its name or its file/module and
# returns error """playwright._impl._errors.Error: It looks like you are using Playwright Sync API inside the asyncio loop. Please use the Async API instead."""
@pytest.mark.skip
@pytest.mark.needs_asyncio_and_pytest_asyncio_and_mark_asyncio
def test_sync_test():
    with sync_playwright() as p:
        browser_context: BrowserContext = p.chromium.launch(headless=True).new_context()
        page = browser_context.new_page()
        page.goto("https://f.ua")
        request_context: APIRequestContext = p.request.new_context(base_url="https://api.github.com")
        response: APIResponse = request_context.get("/outlander/repos", ignore_https_errors=True, max_redirects=5)
        assert not response.ok
        assert response.status == 404
        assert response.status_text == "Not Found"
        assert response.headers["content-type"] == "application/json; charset=utf-8"
        assert response.json()["message"] == "Not Found"
        assert response.body() == b'{"message":"Not Found","documentation_url":"https://docs.github.com/rest","status":"404"}'