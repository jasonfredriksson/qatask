import re
from playwright.sync_api import Page, expect
from pages.login.login_locators import LoginLocators

class LoginValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginLocators(page)
    
    def verify_page_loaded(self):
        expect(self.page).to_have_title("XYZ Bank")
        expect(self.page).to_have_url(re.compile(r".*#/login"))
