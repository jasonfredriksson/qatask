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
    
    def verify_customer_login_button_visible(self):
        expect(self.locators.customer_login_button).to_be_visible()
        expect(self.locators.customer_login_button).to_be_enabled()
    
    def verify_bank_manager_login_button_visible(self):
        expect(self.locators.bank_manager_login_button).to_be_visible()
        expect(self.locators.bank_manager_login_button).to_be_enabled()
    
    def verify_all_buttons_visible(self):
        self.verify_customer_login_button_visible()
        self.verify_bank_manager_login_button_visible()
