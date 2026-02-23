from playwright.sync_api import Page, expect
from pages.manager.manager_locators import ManagerLocators

class ManagerValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ManagerLocators(page)
    
    def verify_manager_page_loaded(self):
        expect(self.page).to_have_url("**/manager")
        expect(self.locators.add_customer_button).to_be_visible()
        expect(self.locators.open_account_button).to_be_visible()
        expect(self.locators.customers_button).to_be_visible()
    
    def verify_add_customer_form_visible(self):
        expect(self.locators.first_name_input).to_be_visible()
        expect(self.locators.last_name_input).to_be_visible()
        expect(self.locators.post_code_input).to_be_visible()
    
    def verify_open_account_form_visible(self):
        expect(self.locators.customer_select_dropdown).to_be_visible()
        expect(self.locators.currency_select_dropdown).to_be_visible()
        expect(self.locators.process_button).to_be_visible()
    
    def verify_customers_table_visible(self):
        expect(self.locators.customers_table).to_be_visible()
    
    def verify_success_message_contains(self, expected_text: str):
        expect(self.locators.success_alert).to_contain_text(expected_text)
    
    def verify_customer_added_successfully(self):
        expect(self.locators.success_alert).to_contain_text("Customer added successfully")
    
    def verify_account_created_successfully(self):
        expect(self.locators.success_alert).to_contain_text("Account created successfully")
    
    def verify_customer_count(self, expected_count: int):
        rows = self.page.locator("tbody tr")
        expect(rows).to_have_count(expected_count)
    
    def verify_customer_exists_in_table(self, customer_name: str):
        expect(self.locators.table_cell_by_text(customer_name)).to_be_visible()
