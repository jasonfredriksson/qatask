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
    
    def add_new_customer(self, first_name: str, last_name: str, post_code: str):
        self.click_add_customer()
        self.locators.first_name_input.fill(first_name)
        self.locators.last_name_input.fill(last_name)
        self.locators.post_code_input.fill(post_code)
        self.locators.add_customer_submit_button.click()
    
    def open_account_for_customer(self, customer_name: str, currency: str):
        self.click_open_account()
        self.locators.customer_select_dropdown.select_option(label=customer_name)
        self.locators.currency_select_dropdown.select_option(label=currency)
        self.locators.process_button.click()
    
    def open_account_by_index(self, customer_index: int, currency: str):
        self.click_open_account()
        self.locators.customer_select_dropdown.select_option(index=customer_index)
        self.locators.currency_select_dropdown.select_option(label=currency)
        self.locators.process_button.click()
    
    def search_customer(self, search_term: str):
        self.locators.search_customer_input.fill(search_term)
    
    def delete_customer_by_index(self, index: int):
        self.locators.delete_button_by_customer_index(index).click()
    
    def get_customer_rows_count(self) -> int:
        return self.page.locator("tbody tr").count()
    
    def get_success_message(self) -> str:
        return self.locators.success_alert.text_content()
    
    def click_home(self):
        self.locators.home_button.click()
        self.page.wait_for_url("**/login")
