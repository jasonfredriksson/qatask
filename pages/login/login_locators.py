from playwright.sync_api import Page, Locator

class LoginLocators:
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def customer_login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customer Login")
    
    @property
    def bank_manager_login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Bank Manager Login")
    
    @property
    def home_button(self) -> Locator:
        return self.page.get_by_role("button", name="Home")
