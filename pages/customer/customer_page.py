from playwright.sync_api import Page
from pages.customer.customer_locators import CustomerLocators
from pages.customer.customer_actions import CustomerActions
from pages.customer.customer_validations import CustomerValidations

class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
        self.actions = CustomerActions(page)
        self.validations = CustomerValidations(page)
