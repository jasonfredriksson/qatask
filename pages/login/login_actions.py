from playwright.sync_api import Page
from pages.base.base_actions import BaseActions
from pages.login.login_locators import LoginLocators

class LoginActions(BaseActions):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = LoginLocators(page)
    
    def navigate(self):
        self.navigate_to("login")
    
    def click_customer_login(self):
        self.locators.customer_login_button.click()
        self.page.wait_for_url("**/customer")
    
    def click_bank_manager_login(self):
        self.locators.bank_manager_login_button.click()
        self.page.wait_for_url("**/manager")
