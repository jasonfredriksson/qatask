from playwright.sync_api import Page
from pages.manager.manager_locators import ManagerLocators
from pages.manager.manager_actions import ManagerActions
from pages.manager.manager_validations import ManagerValidations

class ManagerPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ManagerLocators(page)
        self.actions = ManagerActions(page)
        self.validations = ManagerValidations(page)
