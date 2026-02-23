from playwright.sync_api import Page
from pages.login.login_locators import LoginLocators
from pages.login.login_actions import LoginActions
from pages.login.login_validations import LoginValidations

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginLocators(page)
        self.actions = LoginActions(page)
        self.validations = LoginValidations(page)
