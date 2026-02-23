import re
from playwright.sync_api import Page, expect
from pages.customer.customer_locators import CustomerLocators

class CustomerValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
    
    def verify_customer_selection_page_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*#/customer"))
        expect(self.locators.your_name_label).to_be_visible()
        expect(self.locators.user_select_dropdown).to_be_visible()
    
    def verify_account_page_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*#/account"))
        expect(self.locators.welcome_message).to_be_visible()
    
    def verify_welcome_message_visible(self):
        expect(self.locators.welcome_message).to_be_visible()
    
    def verify_account_number_visible(self):
        expect(self.locators.account_number).to_be_visible()
    
    def verify_balance_visible(self):
        expect(self.locators.balance).to_be_visible()
    
    def verify_all_account_buttons_visible(self):
        expect(self.locators.transactions_button).to_be_visible()
        expect(self.locators.deposit_button).to_be_visible()
        expect(self.locators.withdrawl_button).to_be_visible()
    
    def verify_deposit_successful(self):
        expect(self.locators.success_message).to_have_text("Deposit Successful")
    
    def verify_withdrawal_successful(self):
        expect(self.locators.success_message).to_have_text("Transaction successful")
    
    def verify_balance_equals(self, expected_balance: str):
        expect(self.locators.balance).to_have_text(expected_balance)
    
    def verify_balance_contains(self, expected_text: str):
        expect(self.locators.balance).to_contain_text(expected_text)
    
    def verify_transactions_table_visible(self):
        expect(self.locators.transactions_table).to_be_visible()
    
    def verify_transaction_count(self, expected_count: int):
        rows = self.page.locator("tbody tr")
        expect(rows).to_have_count(expected_count)
