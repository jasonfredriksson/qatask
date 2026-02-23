from playwright.sync_api import Page
from pages.customer.customer_locators import CustomerLocators

class CustomerActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
    
    def select_user_by_name(self, name: str):
        self.locators.user_select_dropdown.select_option(label=name)
    
    def click_login(self):
        self.locators.login_button.click()
        self.page.wait_for_url("**/account")
    
    def click_deposit(self):
        self.locators.deposit_button.click()
        self.locators.deposit_label.wait_for(state="visible", timeout=3000)
    
    def fill_deposit_amount(self, amount: str):
        self.locators.amount_input.fill(amount)
    
    def confirm_deposit(self):
        self.locators.deposit_confirm_button.click()
    
    def click_withdrawal(self):
        self.locators.withdrawl_button.click()
        self.locators.withdrawal_label.wait_for(state="visible", timeout=3000)
    
    def fill_withdrawal_amount(self, amount: str):
        self.locators.amount_input.clear()
        self.locators.amount_input.fill(amount)
    
    def confirm_withdrawal(self):
        self.locators.withdraw_confirm_button.click()
    
    def get_balance_text(self) -> str:
        return self.locators.balance.text_content()
