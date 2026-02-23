from playwright.sync_api import Page, Locator

class BaseLocators:
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def home_button(self) -> Locator:
        return self.page.get_by_role("button", name="Home")
    
    @property
    def logout_button(self) -> Locator:
        return self.page.get_by_role("button", name="Logout")
