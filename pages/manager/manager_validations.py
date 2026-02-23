import re
from playwright.sync_api import Page, expect
from pages.manager.manager_locators import ManagerLocators

class ManagerValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ManagerLocators(page)
    
    def verify_manager_page_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*#/manager"))
        expect(self.locators.add_customer_button).to_be_visible()
        expect(self.locators.open_account_button).to_be_visible()
        expect(self.locators.customers_button).to_be_visible()
    
    def verify_customer_in_table(self, first_name: str, last_name: str):
        customer_row = self.page.locator(f"tbody tr:has-text('{first_name}'):has-text('{last_name}')").last
        expect(customer_row).to_be_visible()
    
    def verify_customer_has_no_account(self, first_name: str, last_name: str):
        customer_row = self.page.locator(f"tbody tr:has-text('{first_name}'):has-text('{last_name}')").last
        account_number_cell = customer_row.locator("td").nth(3)
        expect(account_number_cell).to_be_empty()
    
    def verify_customer_has_account(self, first_name: str, last_name: str):
        customer_row = self.page.locator(f"tbody tr:has-text('{first_name}'):has-text('{last_name}')").last
        account_number_cell = customer_row.locator("td").nth(3)
        expect(account_number_cell).not_to_be_empty()
    
    def verify_customer_not_in_table(self, first_name: str, last_name: str, postcode: str):
        customer_row = self.page.locator(f"tbody tr:has-text('{first_name}'):has-text('{last_name}'):has-text('{postcode}')")
        expect(customer_row).not_to_be_visible()
