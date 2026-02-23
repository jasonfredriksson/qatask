from playwright.sync_api import Page
from pages.manager.manager_locators import ManagerLocators

class ManagerActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ManagerLocators(page)
    
    def click_add_customer(self):
        self.locators.add_customer_button.click()
    
    def click_open_account(self):
        self.locators.open_account_button.click()
    
    def click_customers(self):
        self.locators.customers_button.click()
    
    def delete_customer(self, first_name: str, last_name: str, postcode: str):
        customer_row = self.page.locator(f"tbody tr:has-text('{first_name}'):has-text('{last_name}'):has-text('{postcode}')")
        delete_button = customer_row.locator("button:has-text('Delete')")
        delete_button.click()
    
    def click_home(self):
        self.locators.home_button.click()
        self.page.wait_for_url("**/login")
