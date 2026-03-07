import pytest
from playwright.sync_api import Page
from pages.login.login_page import LoginPage
from pages.customer.customer_page import CustomerPage

class TestNegativeScenarios:
    """Test negative scenarios and edge cases for customer operations"""
    
    def test_withdrawal_exceeds_balance_overdraft(self, page: Page, test_data):
        """Test that withdrawal fails when amount exceeds available balance"""
        print("\n[INFO] Starting test: Withdrawal exceeds balance (overdraft)")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['hermoine_granger']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Getting current balance")
        balance_text = customer_page.actions.get_balance_text()
        current_balance = int(balance_text)
        
        print(f"[INFO] Current balance: {current_balance}")
        overdraft_amount = str(current_balance + 10000)
        
        print(f"[INFO] Attempting to withdraw {overdraft_amount} (exceeds balance)")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount(overdraft_amount)
        customer_page.actions.confirm_withdrawal()
        
        print("[INFO] Verifying overdraft error message appears")
        # The application should show an error or prevent the withdrawal
        error_message = page.locator("span[ng-show='message']")
        error_message.wait_for(state="visible", timeout=5000)
        
        # Verify the error message indicates transaction failed
        message_text = error_message.text_content()
        assert "fail" in message_text.lower() or "insufficient" in message_text.lower(), \
            f"Expected error message for overdraft, got: {message_text}"
        
        print("[INFO] Verified overdraft is prevented")
        print("[INFO] Test completed successfully")
    
    def test_deposit_with_empty_amount(self, page: Page, test_data):
        """Test that deposit fails with empty amount field"""
        print("\n[INFO] Starting test: Deposit with empty amount")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['harry_potter']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Attempting deposit with empty amount")
        customer_page.actions.click_deposit()
        
        # Try to submit without entering amount
        customer_page.actions.confirm_deposit()
        
        print("[INFO] Verifying deposit button behavior with empty input")
        # The form should either prevent submission or show validation error
        # Check if we're still on the account page (form didn't submit)
        current_url = page.url
        assert "#/account" in current_url, "Should remain on account page with invalid input"
        
        print("[INFO] Verified empty amount is handled correctly")
        print("[INFO] Test completed successfully")
    
    def test_withdrawal_with_zero_amount(self, page: Page, test_data):
        """Test that withdrawal fails with zero amount"""
        print("\n[INFO] Starting test: Withdrawal with zero amount")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['ron_weasly']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Getting initial balance")
        initial_balance = int(customer_page.actions.get_balance_text())
        
        print("[INFO] Attempting withdrawal with zero amount")
        customer_page.actions.click_withdrawal()
        customer_page.actions.fill_withdrawal_amount("0")
        customer_page.actions.confirm_withdrawal()
        
        # Wait a moment for any processing
        page.wait_for_timeout(1000)
        
        print("[INFO] Verifying balance unchanged")
        final_balance = int(customer_page.actions.get_balance_text())
        
        assert initial_balance == final_balance, \
            f"Balance should not change with zero withdrawal. Initial: {initial_balance}, Final: {final_balance}"
        
        print("[INFO] Verified zero amount withdrawal is handled correctly")
        print("[INFO] Test completed successfully")
    
    def test_deposit_with_negative_amount(self, page: Page, test_data):
        """Test that deposit fails with negative amount"""
        print("\n[INFO] Starting test: Deposit with negative amount")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['harry_potter']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Getting initial balance")
        initial_balance = int(customer_page.actions.get_balance_text())
        
        print("[INFO] Attempting deposit with negative amount")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount("-1000")
        customer_page.actions.confirm_deposit()
        
        # Wait a moment for any processing
        page.wait_for_timeout(1000)
        
        print("[INFO] Verifying balance unchanged or error shown")
        final_balance = int(customer_page.actions.get_balance_text())
        
        # Balance should either remain the same or the form should prevent submission
        assert initial_balance == final_balance, \
            f"Balance should not change with negative deposit. Initial: {initial_balance}, Final: {final_balance}"
        
        print("[INFO] Verified negative amount deposit is handled correctly")
        print("[INFO] Test completed successfully")
    
    def test_deposit_with_invalid_characters(self, page: Page, test_data):
        """Test that HTML5 input validation prevents non-numeric input"""
        print("\n[INFO] Starting test: Deposit with invalid characters (HTML5 validation)")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['hermoine_granger']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Clicking deposit button")
        customer_page.actions.click_deposit()
        
        print("[INFO] Verifying input field type is 'number'")
        amount_input = customer_page.locators.amount_input
        input_type = amount_input.get_attribute("type")
        
        assert input_type == "number", \
            f"Amount input should be type='number' for HTML5 validation. Got: {input_type}"
        
        print("[INFO] Verified HTML5 input validation is in place")
        print("[INFO] Input type='number' prevents non-numeric characters at browser level")
        print("[INFO] Test completed successfully")
    
    def test_very_large_deposit_boundary(self, page: Page, test_data):
        """Test deposit with very large amount (boundary testing)"""
        print("\n[INFO] Starting test: Very large deposit (boundary)")
        login_page = LoginPage(page)
        customer_page = CustomerPage(page)
        
        customer_name = test_data['customers']['ron_weasly']
        
        print("[INFO] Navigating to application")
        login_page.actions.navigate()
        login_page.actions.click_customer_login()
        
        print(f"[INFO] Selecting user: {customer_name}")
        customer_page.actions.select_user_by_name(customer_name)
        customer_page.actions.click_login()
        
        print("[INFO] Getting initial balance")
        initial_balance = int(customer_page.actions.get_balance_text())
        
        # Test with a very large amount
        large_amount = "999999999"
        
        print(f"[INFO] Attempting deposit with large amount: {large_amount}")
        customer_page.actions.click_deposit()
        customer_page.actions.fill_deposit_amount(large_amount)
        customer_page.actions.confirm_deposit()
        
        print("[INFO] Waiting for transaction to process")
        page.wait_for_timeout(2000)
        
        print("[INFO] Verifying transaction result")
        final_balance = int(customer_page.actions.get_balance_text())
        
        # Either the transaction succeeds or is rejected
        # If it succeeds, balance should increase by the large amount
        # If it fails, balance should remain the same
        if final_balance > initial_balance:
            expected_balance = initial_balance + int(large_amount)
            assert final_balance == expected_balance, \
                f"If large deposit succeeds, balance should be correct. Expected: {expected_balance}, Got: {final_balance}"
            print(f"[INFO] Large deposit succeeded. New balance: {final_balance}")
        else:
            assert final_balance == initial_balance, \
                f"If large deposit fails, balance should remain unchanged. Initial: {initial_balance}, Final: {final_balance}"
            print("[INFO] Large deposit was rejected (acceptable behavior)")
        
        print("[INFO] Test completed successfully")
