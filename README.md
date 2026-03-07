# Banking App Automation Suite

A comprehensive test automation suite using Python and Playwright for testing the AngularJS Banking Project application. Built with the **Page Object Model (POM)** design pattern with separate Locators, Actions, and Validations layers for maximum reusability and maintainability.

## Features

- **Enhanced Page Object Model** - Separate Locators, Actions, and Validations layers with full base class inheritance
- **Centralized Configuration** - Environment-based configuration using python-dotenv
- **Comprehensive Test Coverage** - Both positive and negative test scenarios including edge cases
- **Playwright's built-in locators** - Auto-wait and auto-retry capabilities with `get_by_role()`, `get_by_text()`, etc.
- **Cross-browser testing** - Chrome, Firefox, Safari support
- **JSON-based test data** - Centralized test data management
- **Full user journey coverage** - Customer & Manager flows with validation scenarios
- **Artifact Generation** - Screenshots, videos, and unique trace files per test
- **Modular test structure** - Clean separation of concerns with DRY principles
- **Granular action methods** - Avoid Playwright strict mode violations

## Test Coverage

### Login Page Tests
- Page load verification
- Button presence and functionality
- Navigation to customer and manager portals

### Customer Operations Tests (Happy Path)
- Login and account verification
- Deposit functionality
- Withdrawal functionality
- Transaction history with balance validation
- Multiple transactions with balance tracking

### Bank Manager Operations Tests (Happy Path)
- Add new customers
- Open accounts
- View customer list
- Delete customers
- Account verification

### Negative & Validation Scenarios
- **Overdraft Protection** - Withdrawal exceeding available balance
- **Empty Input Validation** - Deposit/withdrawal with empty amount
- **Zero Amount Handling** - Transactions with zero value
- **Negative Amount Validation** - Deposits with negative values
- **HTML5 Input Validation** - Non-numeric input prevention
- **Boundary Testing** - Very large amounts (999,999,999)

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js (for Playwright browsers)

### Installation

1. **Clone or create the project directory**

2. **Configure environment variables:**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your configuration (URL, browser settings, etc.)
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

### Running Tests

Playwright for Python uses pytest as its test runner with built-in features for screenshots, videos, and traces.

#### Run all tests (default configuration from pytest.ini):
```bash
pytest
```

#### Run specific test file:
```bash
pytest tests/test_customer_workflows.py
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

#### Run specific test method:
```bash
pytest tests/test_customer_workflows.py::TestCustomerWorkflows::test_deposit_with_success_message
```

#### View trace files (for debugging):
```bash
playwright show-trace test-results/trace.zip
```

## Reports and Artifacts

Playwright automatically generates test artifacts in the `test-results/` directory:

### Screenshots
- Automatically captured on test failures
- Saved in `test-results/`

### Videos
- Recorded for failed tests (configurable)
- Saved in `test-results/videos/`

### Traces
- Interactive trace files with timeline, screenshots, and network activity
- Saved as `test-results/trace.zip`
- View with: `playwright show-trace test-results/trace.zip`
- Provides detailed debugging information including:
  - DOM snapshots at each action
  - Network requests
  - Console logs
  - Screenshots at each step

## Project Structure

```
banking-automation/
├── pages/                         # Page Object Model classes
│   ├── base/
│   │   ├── base_locators.py      # Common locators (Home, Logout)
│   │   ├── base_actions.py       # Common actions
│   │   └── base_validations.py   # Common validations
│   ├── login/
│   │   ├── login_locators.py     # Login page element locators
│   │   ├── login_actions.py      # Login page actions
│   │   ├── login_validations.py  # Login page validations
│   │   └── login_page.py         # Login page facade
│   ├── customer/
│   │   ├── customer_locators.py  # Customer page element locators
│   │   ├── customer_actions.py   # Customer page actions
│   │   ├── customer_validations.py # Customer page validations
│   │   └── customer_page.py      # Customer page facade
│   └── manager/
│       ├── manager_locators.py   # Manager page element locators
│       ├── manager_actions.py    # Manager page actions
│       ├── manager_validations.py # Manager page validations
│       └── manager_page.py       # Manager page facade
├── tests/
│   ├── test_customer_workflows.py # Customer workflow tests (happy path)
│   ├── test_manager_workflows.py  # Manager workflow tests (happy path)
│   ├── test_negative_scenarios.py # Negative and validation test scenarios
│   ├── test_data.json            # Centralized test data
│   └── conftest.py               # Pytest fixtures and configuration
├── test-results/                 # Playwright test artifacts
│   ├── traces/                   # Unique trace file per test
│   ├── videos/                   # Test execution videos
│   └── screenshots/              # Failure screenshots
├── .env                          # Environment configuration (gitignored)
├── .env.example                  # Environment template
├── pytest.ini                    # Pytest configuration with Playwright settings
├── playwright.config.py          # Playwright browser and context configuration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Page Object Model Architecture

### Enhanced 3-Layer Structure with Base Class Inheritance

This project uses an enhanced Page Object Model with three distinct layers, all inheriting from base classes:

1. **Locators** - Element selectors and locator methods
   - All inherit from `BaseLocators` (eliminates duplicate locators)
2. **Actions** - User interactions and workflows
   - All inherit from `BaseActions` (centralizes navigation and common actions)
3. **Validations** - Assertions and verification methods
   - All inherit from `BaseValidations` (shares common validation patterns)

**Inheritance Hierarchy:**
```
BaseLocators → LoginLocators, CustomerLocators, ManagerLocators
BaseActions → LoginActions, CustomerActions, ManagerActions
BaseValidations → LoginValidations, CustomerValidations, ManagerValidations
```

This separation provides:
- **DRY Principle** - No code duplication, everything inherited from base classes
- **Clear responsibility** - Each file has a single, well-defined purpose
- **Easy maintenance** - Changes to UI only affect locators, common logic in base classes
- **Centralized configuration** - URL and settings managed through `BaseActions` using .env
- **Reusability** - Actions and validations can be composed in different ways
- **Testability** - Each layer can be tested independently

### Layer Details

#### Locators Layer
Contains all element selectors using Playwright's built-in locators:
```python
class CustomerLocators:
    @property
    def deposit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Deposit")
    
    @property
    def amount_input(self) -> Locator:
        return self.page.get_by_placeholder("amount")
```

#### Actions Layer
Contains methods that perform user interactions:
```python
class CustomerActions:
    def click_deposit(self):
        self.locators.deposit_button.click()
        self.locators.deposit_label.wait_for(state="visible", timeout=3000)
    
    def fill_deposit_amount(self, amount: str):
        self.locators.amount_input.fill(amount)
    
    def confirm_deposit(self):
        self.locators.deposit_confirm_button.click()
```

#### Validations Layer
Contains assertion methods for verifying page state:
```python
class CustomerValidations:
    def verify_deposit_successful(self):
        self.locators.success_message.wait_for(state="visible", timeout=5000)
        expect(self.locators.success_message).to_have_text("Deposit Successful")
```

#### Page Facade
Combines all three layers into a single interface:
```python
class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
        self.actions = CustomerActions(page)
        self.validations = CustomerValidations(page)
```

### Example Usage

```python
from pages.login.login_page import LoginPage
from pages.customer.customer_page import CustomerPage

def test_customer_deposit(page: Page, test_data):
    # Initialize page objects
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    
    # Get test data from JSON
    customer_name = test_data['customers']['hermoine_granger']
    deposit_amount = test_data['amounts']['deposit_small']
    
    # Navigate and login
    login_page.actions.navigate()
    login_page.actions.click_customer_login()
    
    # Select user and login
    customer_page.actions.select_user_by_name(customer_name)
    customer_page.actions.click_login()
    
    # Perform deposit with granular methods
    customer_page.actions.click_deposit()
    customer_page.actions.fill_deposit_amount(deposit_amount)
    customer_page.actions.confirm_deposit()
    
    # Verify success
    customer_page.validations.verify_deposit_successful()
```

## Configuration

### pytest.ini
Main test configuration file with Playwright settings:
- Browser selection (chromium, firefox, webkit)
- Headed/headless mode
- Screenshot capture settings
- Video recording options
- Trace generation settings
- Test discovery patterns

### playwright.config.py
Playwright-specific configuration:
- Browser launch arguments (viewport size, slow motion)
- Browser context settings (video recording, tracing)
- Automatic tracing for all tests

### conftest.py
Contains shared pytest fixtures:
- `page` fixture for browser setup/teardown
- `test_data` fixture for loading JSON test data

### test_data.json
Centralized test data including:
- Customer names
- Manager customer data
- Transaction amounts
- Currencies
- Validation messages

## Framework Improvements

This framework has been built with production-quality standards addressing common automation pitfalls:

### ✅ Base Class Inheritance
**All page objects inherit from base classes** - eliminates code duplication and centralizes common functionality:
- `LoginLocators`, `CustomerLocators`, `ManagerLocators` → inherit from `BaseLocators`
- `LoginActions`, `CustomerActions`, `ManagerActions` → inherit from `BaseActions`
- `LoginValidations`, `CustomerValidations`, `ManagerValidations` → inherit from `BaseValidations`

**Benefits:**
- No duplicate `home_button` locators or `click_home()` methods
- Centralized URL management through `BaseActions`
- DRY principle applied throughout

### ✅ Centralized Configuration
**Environment-based configuration using python-dotenv:**
- `.env` file contains all configuration (BASE_URL, browser settings)
- `.env.example` provided as template
- No hardcoded URLs anywhere in codebase
- Easy environment switching (dev, staging, prod)

### ✅ Proper Artifact Pipeline
**Uses pytest-playwright's built-in fixtures** instead of custom implementations:
- Removed custom `page` fixture that bypassed artifact generation
- Screenshots automatically captured on failures
- Videos recorded for failed tests
- Unique trace files generated per test (not overwritten)

### ✅ Comprehensive Test Coverage
**14 tests total: 8 happy path + 6 negative scenarios**

**Negative & Validation Scenarios:**
- Overdraft protection (withdrawal exceeding balance)
- Empty input validation
- Zero amount handling
- Negative amount validation
- HTML5 input validation (type="number")
- Boundary testing (very large amounts)

## Best Practices Used

1. **Enhanced Page Object Model** - Separate Locators, Actions, and Validations layers
2. **Playwright Built-in Locators** - Using `get_by_role()`, `get_by_text()`, `get_by_placeholder()` for robust element selection
3. **Granular Action Methods** - Individual methods for each step to avoid Playwright strict mode violations
4. **JSON Test Data** - Centralized test data management with `test_data.json`
5. **Auto-wait & Auto-retry** - Playwright automatically waits for elements to be actionable
6. **Element-based Waits** - No arbitrary `wait_for_timeout()` calls, only waits for specific elements
7. **Validation Methods** - No direct locator usage in tests, all validations through methods
8. **Console Logging** - Detailed logging for each test step for better debugging
9. **Balance Validation** - Tests validate actual balance changes instead of unreliable transaction tables

## Debugging

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

## Adding New Tests

1. Create new test file in `tests/` directory with `test_` prefix
2. Use existing fixtures and utilities from `conftest.py` and `utils.py`
3. Follow naming conventions:
   - Test classes: `Test*`
   - Test methods: `test_*`
4. Use Playwright's `expect` API for assertions
5. Add descriptive docstrings for each test
