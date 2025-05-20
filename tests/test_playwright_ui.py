import os
import re
from typing import Dict
from attr import asdict
from playwright.sync_api import Page, expect, Playwright, Browser, Route, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback
from _pytest.fixtures import SubRequest
import pytest

#FIXTURES
#read pytest/fixtures.py line 1243 or look there for "def fixture" description
#tests: test modules or classes can use the ``pytest.mark.usefixtures(fixturename)`` marker

@pytest.fixture(name="testpage")
def fixture_testpage(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({"width":2000, "height":1000})
    yield page
    page.close()

@pytest.fixture(scope="session", name="sub_request")
def fixture_sub_request(request: SubRequest):
    current_folder = os.getcwd()
    downloads_folder = os.path.join(current_folder, "Downloaded")
    if request.config.getoption("--browser") == "firefox":
        return {"downloads_path": f"{downloads_folder}/Firefox"}
    if request.config.getoption("--browser") == "webkit":
        return {"downloads_path": f"{downloads_folder}/Webkit"}
    if request.config.getoption("--browser") == "chromium":
        return {"downloads_path": f"{downloads_folder}/Chromium"}
    else:
        return {"downloads_path": f"{downloads_folder}/Default"}

@pytest.fixture(scope="function", autouse=True, name="before_each_after_each")
def fixture_before_each_after_each(page: Page, request: pytest.FixtureRequest):
    print("Before the test function runs")
    # use the request object in your fixture to check the markers used on the test, and don't do anything if a specific marker is set
    if 'no_before_each_after_each' in request.keywords:
        print("\n----Not applying before_each_after_each autoused fixture to test_list_playwright_devices test fuction----\n")
        yield
    else:
        # Go to the starting url before each test, if autouse=True parameter/value pair is explicitly given in kwargs
        page.goto("https://playwright.dev/")
        yield
        print("\nAfter the test function runs")

@pytest.fixture(scope="session", name="browser_type_launch_args", autouse=True)
def fixture_browser_type_launch_args(browser_type_launch_args: dict, sub_request):
    return {
        **browser_type_launch_args,
        **sub_request,
        "headless": False
    }

@pytest.fixture(scope="function", name="browser_context_args")
def fixture_browser_context_args(browser_context_args: dict):
    return {
        **browser_context_args,
        #takes precedence over default 1280x720, but does not take precedence over @pytest.mark.browser_context_args(viewport={"width": 1920,"height": 900})
        #1728 × 1117 (Rendered as 3456 × 2234, default and native) on Macbook 16-inch, 2021
        "viewport": {
            "width": 1728,
            "height": 992
        }
    }

@pytest.fixture(name="indirect_fixture")
def fixture_indirect_fixture(page, request: pytest.FixtureRequest):
    param = request.param
    if param == "google":
        page.goto("https://google.co.uk")
        return page
    else:
        page.goto("https://yahoo.com")
        return page

@pytest.fixture(name="seeded_indirect_page_fixture")
def fixture_seeded_indirect_page_fixture(page, request: pytest.FixtureRequest):
    param = request.param
    if param[0] == "ask":
        page.goto("https://ask.com")
        return page
    if param[0] == "baidu":
        page.goto("https://www.baidu.com")
        return page
    elif param[0] == "google":
        page.goto("https://google.co.uk")
        return page    

#@pytest.fixture(name="seeded_indirect_title_fixture")
#def fixture_seeded_indirect_title_fixture(request: pytest.FixtureRequest):
#    param = request.param
#    if param[0] == "ask":
#        return str("Ask.com - What's Your Question?")
#    if param[0] == "baidu":
#        return str("百度一下，你就知道")
#    elif param[0] == "google":
#        return str("Google")

#fixture for mobile testing on mobile layout
#@pytest.fixture(scope="function")
#def browser_context_args(browser_context_args: dict, playwright: Playwright):
#    iphone_11 = playwright.devices['iPhone 11 Pro']
#    return {
#        **browser_context_args,
#        **iphone_11
#    }

#HELPERES
def switch_the_page(page: Page, url: str = None):
    expect(page).to_have_url("https://playwright.dev/")
    if page.url == "https://playwright.dev/":
        print(f"Moving from https://playwright.dev/ to {url}\n")
        page.goto(url)
    else:
        page.goto(url)

def generate_pairs(): 
    pairs = []
    users = ["alan", "wake"]
    passwords = ["pass1", "pass2"]
    for user in users:
        for password in passwords:
            pairs.append(pytest.param((user,password), id=f"{user}, {password}"))
    return pairs

def get_argvalues():
    #parametrized_search_engines = []
    search_engines_names = ["google","baidu","ask"]
    search_engines_titles = ["Google","百度一下，你就知道","Ask.com - What's Your Question?"]
    #for engine in search_engines:
    #    parametrized_search_engines.append(pytest.param((engine), id=f"{engine}"))
    parametrized_search_engines = list(zip(search_engines_names,search_engines_titles))
    return parametrized_search_engines

#TESTS
#@pytest.mark.browser_context_args()
#def test_mobile_browser_context_args(page: Page):
#    page.goto("https://github.com")
#    print(page.title())

#@pytest.mark.browser_context_args() #if no viewport given as argument, then def browser_context_args fuction/fixture "viewport" is used if present
#@pytest.mark.browser_context_args(viewport={"width": 1920,"height": 900}) with viewport parameter takes precedence both:
# over default 1280x720 viewport values and 
# over def browser_context_args fuction/fixture "viewport" values if present
@pytest.mark.browser_context_args(viewport={"width": 1920,"height": 900}) #higher priority than "viewport" from def browser_context_args fuction/fixture
def test_fixture_browser_context_args(page: Page, playwright: Playwright, browser: Browser):
    print(len(browser.contexts))
    print(browser.contexts[0].cookies())
    browser.contexts[0].add_cookies([{"name": "INITIAL", "value": "INITIAL_VALUE", "url": "https://playwright.dev", "expires": -1, "httpOnly": False, "secure": False, "sameSite": "None"}])
    print(browser.contexts[0].cookies())
    print(page.viewport_size)
    #new page with new context with new viewport values
    new_browser = playwright.chromium
    launched_new_browser = new_browser.launch(headless=True)
    launched_new_browser_context = launched_new_browser.new_context(viewport={"width": 1600,"height": 1380})
    launched_new_browser_context_page = launched_new_browser_context.new_page() # higher priority than @pytest.mark.browser_context_args(viewport={"width": 1920,"height": 900})
    print(len(launched_new_browser.contexts))
    print(launched_new_browser.contexts[0].cookies())
    print(launched_new_browser_context.cookies())
    print(launched_new_browser_context_page.viewport_size)
    launched_new_browser_context_page.on("request", lambda request: print(request.all_headers()) if re.match(r"https://reqres.in/api/users*", request.url) else print(request.url))
    launched_new_browser_context_page.goto("https://reqres.in/")
    print(launched_new_browser.contexts[0].cookies())
    launched_new_browser.contexts[0].add_cookies([{"name": "SECOND", "value": "SECOND_VALUE", "url": "https://reqres.in", "expires": -1, "httpOnly": False, "secure": False, "sameSite": "None"}])
    print(launched_new_browser_context.cookies())
    launched_new_browser_context_page.set_viewport_size({"width": 640, "height": 480})
    print(launched_new_browser_context_page.viewport_size)
    launched_new_browser_context_page.wait_for_timeout(1000)
    print("\nBefore closing page from second browsercontext --------")
    launched_new_browser_context_page.close()
    print("\nAfter closing page from second browsercontext --------")
    print("\nBefore closing second browsercontext --------")
    launched_new_browser_context.close()
    print("\nAfter closing second browsercontext --------")
    print("--------------------------------- viewport test ended --------------------------------")

@pytest.mark.browser_context_args(locale="de-DE")
def test_mark_browser_context_args(page: Page):
    client_language: str = page.evaluate("window.navigator.language")
    print(client_language)
    assert page.evaluate("window.navigator.language") == "de-DE"

def test_playwright_fixture(page: Page) -> None:
    # Example using expect API
    expect(page).to_have_url(re.compile(r"https://playwright.dev/", re.IGNORECASE))
    print(page.title())

def test_cryptocommercial_io_navigation(page: Page) -> None:
    #Using switch_the_page function instead of commented if/else condition
    switch_the_page(page, "http://cryptocommercial.io/")
    #expect(page).to_have_url("https://playwright.dev/")
    #if page.url == "https://playwright.dev/":
    #    print("Moving from https://playwright.dev/ to http://cryptocommercial.io/\n")
    #    page.goto("http://cryptocommercial.io/")
    #else:
    #    page.goto("http://cryptocommercial.io/")
    page.get_by_role("link", name="Kontakt").click()
    expect(page.get_by_text("Formularz kontaktowy")).to_be_visible()
    #page.locator("//*[@id='wpcf7-f12-o1']/form/div[2]/div[1]/p/label/span/input//div[2]").click()
    expect(page.locator("body > main > section > div > div > div:nth-child(1) > p"))\
        .to_have_text("Wsparcie CryptoCommercial jest online 24 godziny na dobę, 7 dni w tygodniu, aby pomóc Ci w zaspokojeniu Twoich potrzeb.")

@pytest.mark.skip_browser("firefox")
@pytest.mark.no_before_each_after_each # using marker to skip loading page.goto("https://playwright.dev/") in autoused def before_each_after_each fuction/fixture
def test_list_playwright_devices(playwright: Playwright):
        #for key, value in playwright.devices.items():
        #    print(key)
        #    for property in value.items():
        #        print(f"{property[0]} = {property[1]}")
        print(f"{len(playwright.devices)}\n")
        print(playwright.devices[("Desktop Firefox")])

def test_second_context(page: Page, context: BrowserContext):
    page.goto("https://nomads.com/")
    with context.expect_page() as new_page_info:
        page.locator("//div[@class='item show grid-side-box item-latest-jobs not-a-place ignore-click']//child::a").first.click()
    link_text = page.locator("//div[@class='item show grid-side-box item-latest-jobs not-a-place ignore-click']//child::a").first.inner_text()
    second_page = new_page_info.value
    second_page.wait_for_load_state('domcontentloaded')
    assert second_page.title() is not ''
    assert link_text in second_page.title()
    #expect(second_page).to_have_title("")    

def test_third_context(page: Page, context: BrowserContext):
    page.goto("https://nomads.com/")
    with context.expect_event("page") as event_info:
        page.locator("//div[@class='item show grid-side-box item-latest-jobs not-a-place ignore-click']//child::a").first.click()
    link_text = page.locator("//div[@class='item show grid-side-box item-latest-jobs not-a-place ignore-click']//child::a").first.inner_text()
    new_page: Page = event_info.value
    new_page.wait_for_load_state('domcontentloaded')
    assert new_page.title() is not ''
    assert link_text in new_page.title()

@pytest.mark.only_browser("chromium")
def test_multiple_contexts(page: Page, new_context: CreateContextCallback):
    switch_the_page(page, "https://reqres.in/")
    #page.goto("https://reqres.in/")
    expect(page).to_have_title("            Reqres - A hosted REST-API ready to respond to your AJAX requests")
    print(page.title())
    page2 = new_context().new_page()
    page2.goto("https://github.com/JoanEsquivel/playwright-python-test-framework")
    expect(page2).not_to_have_title("JoanEsquivel/playwright-python-test-framework: Repository to track playwright tests")
    print(page2.title())

@pytest.mark.slow
def test_cryptocommercial_io_contact_form_filled(page: Page) -> None:
    switch_the_page(page, "https://cryptocommercial.io/pl/")
    #page.goto("https://cryptocommercial.io/pl/")
    page.hover(".lang_wallet--curency")
    expect(page.get_by_role("link", name="USD")).to_be_visible()
    page.get_by_role("link", name="USD").click()
    page.hover("div.lang_wallet--planet > svg")
    expect(page.get_by_role("link", name="ENG")).to_be_visible()
    page.get_by_role("link", name="ENG").click()
    page.get_by_role("link", name="About", exact=True).click()
    expect(page.get_by_role("main")).to_contain_text("Who we are?")

@pytest.mark.skip
def test_cryptocommercial_io_registration_written_with_codegen_and_debugged_with_inspector(page: Page) -> None:
    switch_the_page(page, "https://cryptocommercial.io/pl/")
    #page.goto("https://cryptocommercial.io/pl/")
    page.hover(".lang_wallet--curency")
    expect(page.get_by_role("link", name="USD")).to_be_visible()
    page.get_by_role("link", name="USD").click()
    page.hover("div.lang_wallet--planet > svg")
    expect(page.get_by_role("link", name="ENG")).to_be_visible()
    page.get_by_role("link", name="ENG").click()
    page.get_by_role("link", name="About", exact=True).click()
    expect(page.get_by_role("main")).to_contain_text("Who we are?")
    page.get_by_role("main").get_by_role("link", name="Register").click()
    expect(page.get_by_text("Welcome to CryptoCommercial!")).to_be_visible()
    expect(page.get_by_role("textbox", name="Name*")).to_be_empty()
    page.get_by_role("textbox", name="Name*").click()
    page.get_by_role("textbox", name="Name*").fill("alanwake")
    expect(page.get_by_role("textbox", name="Email*")).to_be_empty()
    page.get_by_role("textbox", name="Email*").click()
    page.get_by_role("textbox", name="Email*").fill("stakejimmy@gmail.com")
    expect(page.get_by_role("textbox", name="Password*", exact=True)).to_be_empty()
    page.get_by_role("textbox", name="Password*", exact=True).click()
    page.get_by_role("textbox", name="Password*", exact=True).fill("test1234")
    expect(page.get_by_role("textbox", name="Confirm new password*")).to_be_empty()
    page.get_by_role("textbox", name="Confirm new password*").click()
    page.get_by_role("textbox", name="Confirm new password*").fill("test1234")
    expect(page.locator("#wppb-form-element-27 div")).to_be_visible()
    page.locator("#wppb-form-element-27 div").click()
    expect(page.get_by_role("button", name="Register")).to_be_visible()
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_text("Email Verification")).to_be_visible()
    expect(page.locator("#mo_site_otp_form")).to_contain_text("There was an error in sending the OTP.")
    expect(page.locator("#mo_site_otp_form")).to_have_text("Email VerificationThere was an error in sending the OTP. " \
    "Please enter a valid email id or contact site Admin." \
    "{{OTP_STYLE}} {{VALIDATE_BUTTON_OTP}} {{REQUIRED_FIELDS}}{{RESEND_OTP}}{{LOADER_IMG}}")
    expect(page.locator("div.mo_customer_validation-modal-body.center > div:nth-child(1)")).to_contain_text("Please check your email. " \
    "The 6-digit verification code was sent to stakejimmy@gmail.com. Pay attention that the code is valid for 10 minutes.")
    assert(page.inner_text("#mo_site_otp_form") == page.locator("#mo_site_otp_form").inner_text())
    page.locator("div.mo_customer_validation-modal-header > a.close").click()
    expect(page.get_by_text("Email Verification")).not_to_be_visible()

#PARAMETRIZED TESTS
@pytest.mark.parametrize("indirect_fixture", ['google'], indirect=True)
def test_parametrized_indirect_fixture(indirect_fixture: Page):
    expect(indirect_fixture).to_have_title("Google")

@pytest.mark.parametrize("credentials", generate_pairs())
def test_parametrized_generated_pairs(page: Page, credentials):
    login, pas = credentials
    page.goto("https://ineed.ua/ua/user/login") 
    page.locator("input[name='email'][type='text']").fill(login)
    page.locator("input[name='password'][type='password']").fill(pas)
    page.locator("button[name='login'][type='submit'][class='form__button button--blick']").click()
    expect(page.locator("span[data-language='login_error_pass']")).to_be_visible()
    expect(page.locator("span[data-language='login_error_pass']")).to_have_text("Невірний логін або пароль")
    assert((page.locator("span[data-language='login_error_pass']").inner_text()) == "Невірний логін або пароль")

@pytest.mark.browser_context_args(timezone_id="Europe/Berlin")
@pytest.mark.parametrize("seeded_indirect_page_fixture", get_argvalues(), indirect=True)
def test_parametrized_seeded_indirect_page_title_fixture(seeded_indirect_page_fixture: Page):
    list_search_engines_titles = ["Google", 
                                  "百度一下，你就知道", 
                                  "Ask.com - What's Your Question?"]
    set_search_engines_titles = set(list_search_engines_titles)
    title = seeded_indirect_page_fixture.title()
    print(title)
    assert seeded_indirect_page_fixture.title() in list_search_engines_titles
    index = list_search_engines_titles.index(title)
    print(index)
    list_search_engines_titles.pop(index)
    print(list_search_engines_titles)

    title = seeded_indirect_page_fixture.title()
    print(title)
    assert seeded_indirect_page_fixture.title() in set_search_engines_titles
    set_search_engines_titles.remove(title)
    print(set_search_engines_titles)

#API route test
def test_route_continue_request_interception_post_raw_data_modified(page):
    
    def handle_auth(route: Route):
        source_data = route.request.post_data
        print(source_data)
        data = source_data.replace("username", "fakeemail") + "&edited=True"
        #data = source_data + "&edited=True"
        print(data)
        route.continue_(post_data=data)

    page.route(re.compile("profile/authenticate"), handler=handle_auth)
    page.goto("https://gymlog.ru/profile/login/")
    page.get_by_label("Пароль ").fill("password")
    page.locator("css=input[id='email']").fill("username")
    page.locator("css=#login-form button[type='submit']").click()
    expect(page.locator("css=div.col-md-12")).to_be_visible()
    expect(page.locator("xpath=//div[@class='alert result alert-danger']")).to_contain_text("Неверно указана электронная почта, логин или пароль.")

#API route test
def test_route_fulfill_response_interception_json_data_modified(page):
    
    def handle_auth(route: Route):
        response = route.fetch()
        json: Dict = response.json()
        print(json)
        json["errors"]["password"][0] = "FAKE RESPONSE"
        print(json)
        print(response.json()["errors"])
        print(json["errors"])
        route.fulfill(json=json)

    page.route(re.compile("profile/authenticate"), handler=handle_auth)
    page.goto("https://gymlog.ru/profile/login/")
    page.get_by_label("Пароль ").fill("password")
    page.locator("css=input[id='email']").fill("username")
    page.locator("css=#login-form button[type='submit']").click()
    expect(page.locator("css=div.col-md-12")).to_be_visible()
    expect(page.locator("xpath=//div[@class='alert result alert-danger']")).to_contain_text("FAKE RESPONSE")
    page.get_by_role("link", name="Забыли пароль?").click()
    page.wait_for_url("https://gymlog.ru/profile/recovery/")
    expect(page).to_have_url("https://gymlog.ru/profile/recovery/")