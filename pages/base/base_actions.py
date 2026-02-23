from playwright.sync_api import Page
from pages.base.base_locators import BaseLocators

class BaseActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BaseLocators(page)
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/"
    
    def navigate_to(self, path: str = ""):
        self.page.goto(f"{self.base_url}{path}")
        self.page.wait_for_load_state("networkidle")
    
    def wait_for_url(self, url_pattern: str):
        self.page.wait_for_url(url_pattern)
    
    def click_home(self):
        self.locators.home_button.click()
        self.wait_for_url("**/login")
    
    def click_logout(self):
        self.locators.logout_button.click()
        self.wait_for_url("**/login")
