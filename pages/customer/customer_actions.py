from playwright.sync_api import Page
from pages.customer.customer_locators import CustomerLocators

class CustomerActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
    
    def select_user_by_name(self, name: str):
        self.locators.user_select_dropdown.select_option(label=name)
    
    def select_user_by_index(self, index: int):
        self.locators.user_select_dropdown.select_option(index=index)
    
    def click_login(self):
        self.locators.login_button.click()
        self.page.wait_for_url("**/account")
    
    def perform_deposit(self, amount: str):
        self.locators.deposit_button.click()
        self.locators.amount_input.fill(amount)
        self.page.get_by_role("button", name="Deposit").click()
    
    def perform_withdrawal(self, amount: str):
        self.locators.withdrawl_button.click()
        self.locators.amount_input.fill(amount)
        self.page.get_by_role("button", name="Withdraw").click()
    
    def click_transactions(self):
        self.locators.transactions_button.click()
    
    def click_logout(self):
        self.locators.logout_button.click()
        self.page.wait_for_url("**/login")
    
    def select_account(self, account_number: str):
        self.locators.account_select_dropdown.select_option(label=account_number)
    
    def get_balance_text(self) -> str:
        return self.locators.balance.text_content()
    
    def get_account_number_text(self) -> str:
        return self.locators.account_number.text_content()
    
    def get_welcome_message_text(self) -> str:
        return self.locators.welcome_message.text_content()
