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
    
    def verify_welcome_message_contains(self, name: str):
        expect(self.locators.welcome_message).to_contain_text(name)
    
    def verify_deposit_successful(self):
        self.locators.success_message.wait_for(state="visible", timeout=5000)
        expect(self.locators.success_message).to_have_text("Deposit Successful")
    
    def verify_withdrawal_successful(self):
        self.locators.success_message.wait_for(state="visible", timeout=5000)
        expect(self.locators.success_message).to_have_text("Transaction successful")
