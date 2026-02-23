from playwright.sync_api import Page
from pages.login.login_locators import LoginLocators

class LoginActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginLocators(page)
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/"
    
    def navigate(self):
        self.page.goto(f"{self.base_url}login")
        self.page.wait_for_load_state("networkidle")
    
    def click_customer_login(self):
        self.locators.customer_login_button.click()
        self.page.wait_for_url("**/customer")
    
    def click_bank_manager_login(self):
        self.locators.bank_manager_login_button.click()
        self.page.wait_for_url("**/manager")
    
    def click_home(self):
        self.locators.home_button.click()
        self.page.wait_for_url("**/login")
