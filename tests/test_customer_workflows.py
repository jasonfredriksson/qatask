import pytest
from playwright.sync_api import Page, expect
from pages.login.login_page import LoginPage
from pages.customer.customer_page import CustomerPage

class TestCustomerWorkflows:
    """Comprehensive customer workflow tests"""
    
    def test_login_and_verify_welcome_message(self, page: Page, test_data):
        """Test that logging in shows the correct user's name on the account page"""
        print("\n[INFO] Starting test: Login and verify welcome message")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['harry_potter']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        
        print("[INFO] Clicking customer login button")
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        
        print("[INFO] Clicking login button")
        customer_page.actions.click_login()
        
        print("[INFO] Verifying account page loaded")
        customer_page.validations.verify_account_page_loaded()
        
        print(f"[INFO] Verifying welcome message contains: {customer_name}")
        customer_page.validations.verify_welcome_message_contains(customer_name)
        
        print("[INFO] Test completed successfully")
    
    def test_deposit_with_success_message(self, page: Page, test_data):
        """Test deposit and validate success message appears"""
        print("\n[INFO] Starting test: Deposit with success message")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['hermoine_granger']
        deposit_amount = test_data['amounts']['deposit_small']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print(f"[INFO] Initiating deposit of {deposit_amount}")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(deposit_amount)
        customer_page.actions.confirm_deposit()
        
        print("[INFO] Verifying deposit success message")
        customer_page.validations.verify_deposit_successful()
        
        print("[INFO] Test completed successfully")
    
    def test_withdrawal_with_success_message(self, page: Page, test_data):
        """Test withdrawal and validate success message appears"""
        print("\n[INFO] Starting test: Withdrawal with success message")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['hermoine_granger']
        deposit_amount = test_data['amounts']['deposit_xlarge']
        withdrawal_amount = test_data['amounts']['withdrawal_large']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print(f"[INFO] Depositing {deposit_amount} first")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(deposit_amount)
        customer_page.actions.confirm_deposit()
        
        print(f"[INFO] Withdrawing {withdrawal_amount}")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount(withdrawal_amount)
        customer_page.actions.confirm_withdrawal()
        
        print("[INFO] Verifying withdrawal success message")
        customer_page.validations.verify_withdrawal_successful()
        
        print("[INFO] Test completed successfully")
    
    def test_multiple_transactions_validate_balance(self, page: Page, test_data):
        """Test that 3 deposits and 3 withdrawals update the balance correctly"""
        print("\n[INFO] Starting test: Multiple transactions with balance validation")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['hermoine_granger']
        amounts = test_data['amounts']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Getting initial balance")
        initial_balance = customer_page.actions.get_balance_text()
        print(f"[INFO] Initial balance: {initial_balance}")
        
        print(f"[INFO] Performing deposit 1: {amounts['deposit_small']}")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(amounts['deposit_small'])
        customer_page.actions.confirm_deposit()
        customer_page.validations.verify_deposit_successful()
        
        print(f"[INFO] Performing deposit 2: {amounts['deposit_medium']}")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(amounts['deposit_medium'])
        customer_page.actions.confirm_deposit()
        customer_page.validations.verify_deposit_successful()
        
        print(f"[INFO] Performing deposit 3: {amounts['deposit_large']}")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(amounts['deposit_large'])
        customer_page.actions.confirm_deposit()
        customer_page.validations.verify_deposit_successful()
        
        print(f"[INFO] Performing withdrawal 1: {amounts['withdrawal_small']}")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount(amounts['withdrawal_small'])
        customer_page.actions.confirm_withdrawal()
        customer_page.validations.verify_withdrawal_successful()
        
        print(f"[INFO] Performing withdrawal 2: {amounts['withdrawal_medium']}")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount(amounts['withdrawal_medium'])
        customer_page.actions.confirm_withdrawal()
        customer_page.validations.verify_withdrawal_successful()
        
        print(f"[INFO] Performing withdrawal 3: {amounts['withdrawal_large']}")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount(amounts['withdrawal_large'])
        customer_page.actions.confirm_withdrawal()
        customer_page.validations.verify_withdrawal_successful()
        
        print("[INFO] Getting final balance")
        final_balance = customer_page.actions.get_balance_text()
        print(f"[INFO] Final balance: {final_balance}")
        
        expected_change = 1000 + 2000 + 3000 - 500 - 750 - 1000
        print(f"[INFO] Expected balance change: {expected_change}")
        
        initial_value = int(initial_balance)
        final_value = int(final_balance)
        actual_change = final_value - initial_value
        
        print(f"[INFO] Actual balance change: {actual_change}")
        assert actual_change == expected_change, f"Balance change mismatch. Expected: {expected_change}, Actual: {actual_change}"
        
        print("[INFO] Test completed successfully")
