from typing import Dict
import pytest
from playwright.async_api import async_playwright, APIRequestContext, APIResponse, Browser, BrowserContext, Page

@pytest.mark.needs_asyncio_and_pytest_asyncio_and_mark_asyncio
@pytest.mark.asyncio
async def test_async_test():
    async with async_playwright() as p:
        browser: Browser = await p.chromium.launch(headless=True)
        browser_context: BrowserContext = await browser.new_context()
        print(browser_context)
        page: Page = await browser.new_page()
        await page.goto("https://f.ua")
        request_context: APIRequestContext = await p.request.new_context(base_url="https://api.github.com")
        response: APIResponse = await request_context.get("/outlander/repos", ignore_https_errors=True, max_redirects=5)
        response_json: Dict = await response.json()
        response_body: bytes = await response.body()
        assert not response.ok
        print(response.ok)
        assert response.status == 404
        assert response.status_text == "Not Found"
        assert response.headers["content-type"] == "application/json; charset=utf-8"
        assert response_json["message"] == "Not Found"
        assert response_json["status"] == "404"
        assert response_body == b'{"message":"Not Found","documentation_url":"https://docs.github.com/rest","status":"404"}'
