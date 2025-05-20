import os
import asyncio
from playwright.async_api import async_playwright, Playwright, APIRequestContext, APIResponse, Browser, BrowserContext, Page, expect
import datetime

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://github.com/outlandergithub")
    await page.locator("//span[normalize-space()='sepoliafaucetpk910de']").click()
    await page.wait_for_url("https://github.com/outlandergithub/sepoliafaucetpk910de")
    assert page.url == "https://github.com/outlandergithub/sepoliafaucetpk910de"
    page_title = await page.title()
    assert page_title == "GitHub - outlandergithub/sepoliafaucetpk910de"
    print(page_title)
    await expect(page.locator("div.Box-sc-g0xbh4-0.QkQOb.js-snippet-clipboard-copy-unpositioned.undefined > article > div > h1")).to_have_text("Automated ETH faucet mining and claiming")
    await browser.close()

REPO = "test-repo-01-"+str(hash(datetime.datetime.now()))
USER = "outlandergithub"
# use GITHUB secrets instead of an empty token string below. use ${{secrets.PET_GITHUB_API_TOKEN_SECRET}}
# os.environ['PET_GITHUB_API_TOKEN'] = ""
# API_TOKEN = os.getenv("PET_GITHUB_API_TOKEN")
API_TOKEN = "${{secrets.PET_GITHUB_API_TOKEN_SECRET}}"

async def run2(playwright: Playwright):
    # This will launch a new browser, create a context and page. When making HTTP
    # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
    # it will automatically set the cookies to the browser page and vice versa.
    browser: Browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
    context: BrowserContext = await browser.new_context(base_url="https://api.github.com")
    api_request_context: APIRequestContext = context.request
    page: Page = await context.new_page()
    await page.goto("https://github.com/outlandergithub")
    await page.locator("//span[normalize-space()='sepoliafaucetpk910de']").click()
    await page.wait_for_url("https://github.com/outlandergithub/sepoliafaucetpk910de")
    page_title = await page.title()
    assert page.url == "https://github.com/outlandergithub/sepoliafaucetpk910de"
    assert page_title == "GitHub - outlandergithub/sepoliafaucetpk910de"
    print(page_title)

    # Alternatively you can create a APIRequestContext manually without having a browser context attached:
    # api_request_context = await playwright.request.new_context(base_url="https://api.github.com")

    # Create a repository.
    response: APIResponse = await api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
        data={"name": REPO},
    )
    response_json = await response.json()
    print("CREATED A REPO")
    assert response.ok
    assert response.status == 201
    print(response.status)
    print(response_json)
    assert response_json["name"] == REPO

    # Delete a repository.
    response = await api_request_context.delete(
        f"/repos/{USER}/{REPO}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            # Add GitHub personal access token.
            "Authorization": f"token {API_TOKEN}",
        },
    )
    response_json = await response.json()
    assert not response.ok
    assert response.status == 403
    print(response.status)
    print(response_json)
    assert response_json["message"] == "Must have admin rights to Repository."
    assert response_json["status"] == "403"
    response_body = await response.body()
    print(response_body)
    #assert await response_body == '{"status": "ok"}'
    print("FORBIDDEN TO DELETE A REPO VIA API ENDPOINT")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
        await run2(playwright)

if __name__ =="__main__":
    asyncio.run(main())