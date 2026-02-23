# Banking App Automation Suite

A comprehensive test automation suite using Python, Playwright, and pytest for testing the AngularJS Banking Project application. Built with the **Page Object Model (POM)** design pattern for maximum reusability and maintainability.

## 🚀 Features

- **Page Object Model (POM)** - Clean separation of page logic and test logic
- **Playwright's built-in locators** - Auto-wait and auto-retry capabilities with `get_by_role()`, `get_by_text()`, etc.
- **Cross-browser testing** (Chrome, Firefox, Safari)
- **Responsive design testing** (Mobile, Tablet, Desktop)
- **Full user journey coverage** (Customer & Manager flows)
- **Detailed HTML reports** with screenshots
- **Modular test structure** with reusable page objects
- **Easy configuration** with pytest settings

## 📋 Test Coverage

### Login Page Tests
- Page load verification
- Button presence and functionality
- Navigation to customer and manager portals

### Customer Operations Tests
- Login and account verification
- Deposit functionality
- Withdrawal functionality
- Transaction history
- Logout functionality

### Bank Manager Operations Tests
- Add new customers
- Open accounts
- View customer list
- Delete customers
- Logout functionality

### Cross-browser & Responsive Tests
- Multiple browser compatibility
- Mobile and tablet viewport testing

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js (for Playwright browsers)

### Installation

1. **Clone or create the project directory**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

### Running Tests

#### Run all tests with HTML report:
```bash
pytest
```

#### Run specific test file:
```bash
pytest tests/test_login.py
```

#### Run tests in specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

#### Run tests in headless mode:
```bash
pytest --headed=false
```

#### Run tests with verbose output:
```bash
pytest -v
```

#### Run specific test method:
```bash
pytest tests/test_customer_operations.py::TestCustomerOperations::test_deposit_functionality
```

## 📊 Reports

After running tests, HTML reports are generated in the `reports/` directory:
- `report.html` - Main test report with detailed results
- Screenshots are automatically captured on failures

## 📁 Project Structure

```
banking-automation/
├── pages/                         # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py              # Base page with common methods
│   ├── login_page.py             # Login page locators and methods
│   ├── customer_page.py          # Customer page locators and methods
│   └── manager_page.py           # Manager page locators and methods
├── tests/
│   ├── test_simple_login.py      # Simple login flow test (POM example)
│   ├── test_login.py             # Login page tests
│   ├── test_customer_operations.py # Customer banking tests
│   ├── test_manager_operations.py  # Manager functionality tests
│   ├── test_cross_browser.py     # Cross-browser tests
│   └── utils.py                  # Test utilities
├── reports/                      # Test reports and screenshots
├── conftest.py                   # pytest configuration and fixtures
├── pytest.ini                    # pytest settings
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🏗️ Page Object Model Architecture

### Why POM?
The Page Object Model pattern provides:
- **Reusability** - Page methods can be used across multiple tests
- **Maintainability** - Changes to UI only require updates in one place
- **Readability** - Tests read like user actions, not technical implementations
- **Reliability** - Playwright's built-in locators with auto-wait and auto-retry

### Page Objects

#### BasePage (`pages/base_page.py`)
Common functionality shared across all pages:
- Navigation methods
- URL waiting
- Page title retrieval

#### LoginPage (`pages/login_page.py`)
Locators and methods for the login page:
- `customer_login_button` - Using `get_by_role("button", name="Customer Login")`
- `bank_manager_login_button` - Using `get_by_role("button", name="Bank Manager Login")`
- `click_customer_login()` - Navigate to customer selection
- `click_bank_manager_login()` - Navigate to manager dashboard

#### CustomerPage (`pages/customer_page.py`)
Locators and methods for customer operations:
- `user_select_dropdown` - Using `locator("#userSelect")` (name="userSelect", id="userSelect")
- `welcome_message` - Using `locator("span.fontBig")`
- `deposit_button` - Using `get_by_role("button", name="Deposit")`
- `withdrawl_button` - Using `get_by_role("button", name="Withdrawl")`
- `amount_input` - Using `get_by_placeholder("amount")`
- `perform_deposit(amount)` - Complete deposit workflow
- `perform_withdrawal(amount)` - Complete withdrawal workflow

#### ManagerPage (`pages/manager_page.py`)
Locators and methods for manager operations:
- `add_customer_button` - Using `get_by_role("button", name="Add Customer")`
- `first_name_input` - Using `get_by_placeholder("First Name")`
- `last_name_input` - Using `get_by_placeholder("Last Name")`
- `post_code_input` - Using `get_by_placeholder("Post Code")`
- `add_new_customer(first_name, last_name, post_code)` - Complete add customer workflow

### Example Usage

```python
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage

def test_customer_deposit(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    
    # Navigate and login
    login_page.navigate()
    login_page.click_customer_login()
    
    # Select user and login
    customer_page.select_user_by_name("Hermoine Granger")
    customer_page.click_login()
    
    # Perform deposit
    customer_page.perform_deposit("1000")
    
    # Verify success
    expect(customer_page.success_message).to_have_text("Deposit Successful")
```

## 🔧 Configuration

### pytest.ini
Contains test configuration including:
- HTML report generation
- Default browser settings
- Test discovery patterns

### conftest.py
Contains shared fixtures:
- `page` fixture for browser setup/teardown
- `base_url` fixture for application URL
- Automatic navigation to login page

## 🎯 Best Practices Used

1. **Page Object Model** - Clear separation between test logic and page interactions
2. **Playwright Built-in Locators** - Using `get_by_role()`, `get_by_text()`, `get_by_placeholder()` for robust element selection
3. **Auto-wait & Auto-retry** - Playwright automatically waits for elements to be actionable
4. **Fixtures** - Reusable setup and teardown
5. **Assertions** - Clear verification with Playwright's expect API
6. **Wait Strategies** - Proper waiting for elements and network states
7. **Error Handling** - Graceful handling of timeouts and failures
8. **Modular Structure** - Organized test files by functionality

## 🐛 Debugging

### Screenshots on Failure
Screenshots are automatically captured when tests fail and saved in the `reports/` directory.

### Debug Mode
Run tests with additional debugging:
```bash
pytest --headed --slowmo 1000
```

### Browser DevTools
Run with browser developer tools:
```bash
pytest --headed --devtools
```

## 📝 Adding New Tests

1. Create new test file in `tests/` directory with `test_` prefix
2. Use existing fixtures and utilities from `conftest.py` and `utils.py`
3. Follow naming conventions:
   - Test classes: `Test*`
   - Test methods: `test_*`
4. Use Playwright's `expect` API for assertions
5. Add descriptive docstrings for each test

## 🔄 Continuous Integration

This test suite can be easily integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions
- name: Run tests
  run: |
    pip install -r requirements.txt
    playwright install
    pytest --browser chromium --headed=false
```

## 🤝 Contributing

1. Follow the existing code style and patterns
2. Add tests for new functionality
3. Update documentation as needed
4. Ensure all tests pass before submitting
