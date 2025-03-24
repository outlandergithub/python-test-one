from playwright.sync_api import Page, expect

def test_cc_io(page: Page):
    page.goto("http://cryptocommercial.io/")
    page.get_by_role("link", name="Kontakt").click()
    expect(page.get_by_text("Formularz kontaktowy")).to_be_visible()
    #page.locator("//*[@id='wpcf7-f12-o1']/form/div[2]/div[1]/p/label/span/input//div[2]").click()
    expect(page.locator("body > main > section > div > div > div:nth-child(1) > p"))\
        .to_have_text("Wsparcie CryptoCommercial jest online 24 godziny na dobę, 7 dni w tygodniu, aby pomóc Ci w zaspokojeniu Twoich potrzeb.")
