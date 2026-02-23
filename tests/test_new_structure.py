import pytest
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from pages.customer.customer_page import CustomerPage

class TestNewStructure:
    """Test demonstrating the new Actions-Locators-Validations structure"""
    
    def test_customer_login_with_new_structure(self, page: Page):
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        login_page.actions.navigate()
        
        login_page.validations.verify_page_loaded()
        login_page.validations.verify_all_buttons_visible()
        
        login_page.actions.click_customer_login()
        
        customer_page.validations.verify_customer_selection_page_loaded()
        
        customer_page.actions.select_user_by_name("Hermoine Granger")
        customer_page.actions.click_login()
        
        customer_page.validations.verify_account_page_loaded()
        customer_page.validations.verify_welcome_message_visible()
        customer_page.validations.verify_account_number_visible()
        customer_page.validations.verify_balance_visible()
        customer_page.validations.verify_all_account_buttons_visible()
    
    def test_deposit_with_new_structure(self, page: Page):
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        customer_page.actions.select_user_by_name("Hermoine Granger")
        customer_page.actions.click_login()
        
        customer_page.actions.perform_deposit("1000")
        
        customer_page.validations.verify_deposit_successful()
    
    def test_using_dynamic_locators(self, page: Page):
        login_page = LoginPage(page)
        
        login_page.actions.navigate()
        
        custom_button = login_page.locators.button_by_name("Customer Login")
        custom_button.click()
        
        page.wait_for_url("**/customer")
