import pytest
from playwright.sync_api import Page, expect
import os

@pytest.fixture(scope="function")
def page(page: Page):
    """Setup and teardown for each test"""
    # Navigate to the banking application
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.wait_for_load_state("networkidle")
    yield page
    # Cleanup if needed
    page.close()

@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/"
