from playwright.sync_api import Page, Locator

class CustomerLocators:
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def user_select_dropdown(self) -> Locator:
        return self.page.locator("#userSelect")
    
    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Login")
    
    @property
    def your_name_label(self) -> Locator:
        return self.page.get_by_text("Your Name :")
    
    @property
    def logout_button(self) -> Locator:
        return self.page.get_by_role("button", name="Logout")
    
    @property
    def welcome_message(self) -> Locator:
        return self.page.locator("span.fontBig")
    
    @property
    def account_number(self) -> Locator:
        return self.page.locator("strong.ng-binding").first
    
    @property
    def balance(self) -> Locator:
        return self.page.locator("strong.ng-binding").nth(1)
    
    @property
    def currency(self) -> Locator:
        return self.page.locator("strong.ng-binding").nth(2)
    
    @property
    def transactions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Transactions")
    
    @property
    def deposit_button(self) -> Locator:
        return self.page.locator("button.btn-lg.tab:has-text('Deposit')")
    
    @property
    def withdrawl_button(self) -> Locator:
        return self.page.get_by_role("button", name="Withdrawl")
    
    @property
    def amount_input(self) -> Locator:
        return self.page.get_by_placeholder("amount")
    
    @property
    def deposit_label(self) -> Locator:
        return self.page.get_by_text("Amount to be Deposited :")
    
    @property
    def withdrawal_label(self) -> Locator:
        return self.page.get_by_text("Amount to be Withdrawn :")
    
    @property
    def deposit_confirm_button(self) -> Locator:
        return self.page.locator("form[ng-submit='deposit()'] button[type='submit']")
    
    @property
    def withdraw_confirm_button(self) -> Locator:
        return self.page.get_by_role("button", name="Withdraw", exact=False).last
    
    @property
    def success_message(self) -> Locator:
        return self.page.locator("span[ng-show='message']")
    
    @property
    def account_select_dropdown(self) -> Locator:
        return self.page.locator("#accountSelect")
