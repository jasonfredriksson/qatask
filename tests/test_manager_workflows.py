import pytest
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from pages.manager.manager_page import ManagerPage

class TestManagerWorkflows:
    """Comprehensive bank manager workflow tests"""
    
    def test_manager_login_and_verify_actions(self, page: Page):
        """Test that Bank Manager login shows correct action buttons"""
        print("\n[INFO] Starting test: Manager login and verify actions")
        login_page = LoginPage(page)
        manager_page = ManagerPage(page)
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        
        print("[INFO] Clicking Bank Manager login button")
        login_page.actions.click_bank_manager_login()
        
        print("[INFO] Verifying manager page loaded")
        manager_page.validations.verify_manager_page_loaded()
        
        print("[INFO] Test completed successfully")
    
    def test_add_customer_and_verify_in_table(self, page: Page, test_data):
        """Test adding a customer and verifying they appear in the customers table"""
        print("\n[INFO] Starting test: Add customer and verify in table")
        login_page = LoginPage(page)
        manager_page = ManagerPage(page)
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_bank_manager_login()
        
        customer = test_data['manager_customers']['john_doe']
        print(f"[INFO] Adding customer: {customer['first_name']} {customer['last_name']}")
        
        manager_page.actions.click_add_customer()
        manager_page.locators.first_name_input.fill(customer['first_name'])
        manager_page.locators.last_name_input.fill(customer['last_name'])
        manager_page.locators.post_code_input.fill(customer['postcode'])
        
        print("[INFO] Submitting customer form")
        page.once("dialog", lambda dialog: dialog.accept())
        manager_page.locators.add_customer_submit_button.click()
        
        print("[INFO] Navigating to customers page")
        manager_page.actions.click_customers()
        
        print("[INFO] Verifying customer appears in table")
        manager_page.validations.verify_customer_in_table(customer['first_name'], customer['last_name'])
        
        print("[INFO] Verifying account number field is empty")
        manager_page.validations.verify_customer_has_no_account(customer['first_name'], customer['last_name'])
        
        print("[INFO] Test completed successfully")
    
    def test_add_account_and_verify_account_number(self, page: Page, test_data):
        """Test adding an account for a customer and verifying account number appears"""
        print("\n[INFO] Starting test: Add account and verify account number")
        login_page = LoginPage(page)
        manager_page = ManagerPage(page)
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_bank_manager_login()
        
        customer = test_data['manager_customers']['jane_smith']
        currency = test_data['currencies']['dollar']
        
        print(f"[INFO] Adding customer: {customer['first_name']} {customer['last_name']}")
        
        manager_page.actions.click_add_customer()
        manager_page.locators.first_name_input.fill(customer['first_name'])
        manager_page.locators.last_name_input.fill(customer['last_name'])
        manager_page.locators.post_code_input.fill(customer['postcode'])
        
        print("[INFO] Submitting customer form")
        page.once("dialog", lambda dialog: dialog.accept())
        manager_page.locators.add_customer_submit_button.click()
        
        print("[INFO] Opening account for customer")
        manager_page.actions.click_open_account()
        
        customer_name = f"{customer['first_name']} {customer['last_name']}"
        manager_page.locators.customer_select_dropdown.select_option(label=customer_name)
        manager_page.locators.currency_select_dropdown.select_option(label=currency)
        
        print(f"[INFO] Processing account with currency: {currency}")
        page.once("dialog", lambda dialog: dialog.accept())
        manager_page.locators.process_button.click()
        
        print("[INFO] Navigating to customers page")
        manager_page.actions.click_customers()
        
        print("[INFO] Verifying customer appears in table with account number")
        manager_page.validations.verify_customer_has_account(customer['first_name'], customer['last_name'])
        
        print("[INFO] Test completed successfully")
    
    def test_delete_customer(self, page: Page, test_data):
        """Test adding and then deleting a customer"""
        print("\n[INFO] Starting test: Delete customer")
        login_page = LoginPage(page)
        manager_page = ManagerPage(page)
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_bank_manager_login()
        
        customer = test_data['manager_customers']['delete_test']
        print(f"[INFO] Adding customer: {customer['first_name']} {customer['last_name']}")
        
        manager_page.actions.click_add_customer()
        manager_page.locators.first_name_input.fill(customer['first_name'])
        manager_page.locators.last_name_input.fill(customer['last_name'])
        manager_page.locators.post_code_input.fill(customer['postcode'])
        
        print("[INFO] Submitting customer form")
        page.once("dialog", lambda dialog: dialog.accept())
        manager_page.locators.add_customer_submit_button.click()
        
        print("[INFO] Navigating to customers page")
        manager_page.actions.click_customers()
        
        print("[INFO] Verifying customer appears in table")
        manager_page.validations.verify_customer_in_table(customer['first_name'], customer['last_name'])
        
        print("[INFO] Deleting customer")
        manager_page.actions.delete_customer(customer['first_name'], customer['last_name'], customer['postcode'])
        
        print("[INFO] Verifying customer is removed from table")
        manager_page.validations.verify_customer_not_in_table(customer['first_name'], customer['last_name'], customer['postcode'])
        
        print("[INFO] Test completed successfully")
