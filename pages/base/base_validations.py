from playwright.sync_api import Page, expect
from pages.base.base_locators import BaseLocators

class BaseValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BaseLocators(page)
    
    def verify_page_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)
    
    def verify_url_contains(self, url_fragment: str):
        expect(self.page).to_have_url(f"**/{url_fragment}")
    
    def verify_home_button_visible(self):
        expect(self.locators.home_button).to_be_visible()
    
    def verify_logout_button_visible(self):
        expect(self.locators.logout_button).to_be_visible()
