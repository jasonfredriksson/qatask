from playwright.sync_api import Page, Locator
from pages.base.base_locators import BaseLocators

class LoginLocators(BaseLocators):
    def __init__(self, page: Page):
        super().__init__(page)
    
    @property
    def customer_login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customer Login")
    
    @property
    def bank_manager_login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Bank Manager Login")
