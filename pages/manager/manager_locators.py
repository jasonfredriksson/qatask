from playwright.sync_api import Page, Locator

class ManagerLocators:
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def add_customer_button(self) -> Locator:
        return self.page.get_by_role("button", name="Add Customer")
    
    @property
    def open_account_button(self) -> Locator:
        return self.page.get_by_role("button", name="Open Account")
    
    @property
    def customers_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customers")
    
    @property
    def home_button(self) -> Locator:
        return self.page.get_by_role("button", name="Home")
    
    @property
    def first_name_input(self) -> Locator:
        return self.page.get_by_placeholder("First Name")
    
    @property
    def last_name_input(self) -> Locator:
        return self.page.get_by_placeholder("Last Name")
    
    @property
    def post_code_input(self) -> Locator:
        return self.page.get_by_placeholder("Post Code")
    
    @property
    def add_customer_submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Add Customer").nth(1)
    
    @property
    def customer_select_dropdown(self) -> Locator:
        return self.page.locator("#userSelect")
    
    @property
    def currency_select_dropdown(self) -> Locator:
        return self.page.locator("#currency")
    
    @property
    def process_button(self) -> Locator:
        return self.page.get_by_role("button", name="Process")
    
    @property
    def success_alert(self) -> Locator:
        return self.page.locator(".alert")
    
    @property
    def customers_table(self) -> Locator:
        return self.page.locator("table.table")
    
    @property
    def search_customer_input(self) -> Locator:
        return self.page.get_by_placeholder("Search Customer")
    
    def button_by_name(self, button_name: str) -> Locator:
        return self.page.get_by_role("button", name=button_name)
    
    def input_by_placeholder(self, placeholder: str) -> Locator:
        return self.page.get_by_placeholder(placeholder)
    
    def customer_row_by_index(self, index: int) -> Locator:
        return self.page.locator(f"tbody tr:nth-child({index + 1})")
    
    def delete_button_by_customer_index(self, index: int) -> Locator:
        return self.page.locator(f"tbody tr:nth-child({index + 1}) button")
    
    def table_cell_by_text(self, text: str) -> Locator:
        return self.page.locator(f"td:has-text('{text}')")
