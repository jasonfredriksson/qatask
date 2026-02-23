# Banking App Automation Suite - Enhanced Architecture

A comprehensive test automation suite using Python, Playwright, and pytest with an **advanced Page Object Model (POM)** design pattern that separates **Actions**, **Locators**, and **Validations** for maximum reusability and maintainability.

## 🏗️ Architecture Overview

### Three-Layer Page Object Model

Each page is divided into three distinct components:

1. **Locators** - Element selectors and dynamic locator methods
2. **Actions** - User interactions and workflows
3. **Validations** - Assertions and verification methods

This separation provides:
- **Clear responsibility** - Each file has a single, well-defined purpose
- **Easy maintenance** - Changes to UI only affect locators
- **Reusability** - Actions and validations can be composed in different ways
- **Testability** - Each layer can be tested independently

## 📁 New Project Structure

```
banking-automation/
├── pages/
│   ├── base/
│   │   ├── __init__.py
│   │   ├── base_locators.py       # Common locators (Home, Logout)
│   │   ├── base_actions.py        # Common actions (navigate, wait)
│   │   └── base_validations.py    # Common validations
│   ├── login/
│   │   ├── __init__.py
│   │   ├── login_locators.py      # Login page element locators
│   │   ├── login_actions.py       # Login page actions
│   │   ├── login_validations.py   # Login page validations
│   │   └── login_page.py          # Facade combining all three
│   ├── customer/
│   │   ├── __init__.py
│   │   ├── customer_locators.py   # Customer page element locators
│   │   ├── customer_actions.py    # Customer page actions
│   │   ├── customer_validations.py # Customer page validations
│   │   └── customer_page.py       # Facade combining all three
│   └── manager/
│       ├── __init__.py
│       ├── manager_locators.py    # Manager page element locators
│       ├── manager_actions.py     # Manager page actions
│       ├── manager_validations.py # Manager page validations
│       └── manager_page.py        # Facade combining all three
├── tests/
│   ├── test_new_structure.py      # Examples using new structure
│   └── ...
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 🎯 Component Details

### Locators Layer

Contains all element selectors using Playwright's built-in locators with **dynamic locator support**.

**Example from `customer_locators.py`:**
```python
class CustomerLocators:
    def __init__(self, page: Page):
        self.page = page
    
    # Static locators
    @property
    def deposit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Deposit")
    
    @property
    def user_select_dropdown(self) -> Locator:
        return self.page.locator("#userSelect")  # name="userSelect", id="userSelect"
    
    # Dynamic locators (like TypeScript example)
    def button_by_name(self, button_name: str) -> Locator:
        return self.page.get_by_role("button", name=button_name)
    
    def transaction_row_by_index(self, index: int) -> Locator:
        return self.page.locator(f"tbody tr:nth-child({index + 1})")
```

### Actions Layer

Contains methods that perform user interactions and workflows.

**Example from `customer_actions.py`:**
```python
class CustomerActions:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
    
    def select_user_by_name(self, name: str):
        self.locators.user_select_dropdown.select_option(label=name)
    
    def click_login(self):
        self.locators.login_button.click()
        self.page.wait_for_url("**/account")
    
    def perform_deposit(self, amount: str):
        self.locators.deposit_button.click()
        self.locators.amount_input.fill(amount)
        self.page.get_by_role("button", name="Deposit").click()
```

### Validations Layer

Contains assertion methods for verifying page state and behavior.

**Example from `customer_validations.py`:**
```python
class CustomerValidations:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
    
    def verify_account_page_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*#/account"))
        expect(self.locators.welcome_message).to_be_visible()
    
    def verify_deposit_successful(self):
        expect(self.locators.success_message).to_have_text("Deposit Successful")
    
    def verify_all_account_buttons_visible(self):
        expect(self.locators.transactions_button).to_be_visible()
        expect(self.locators.deposit_button).to_be_visible()
        expect(self.locators.withdrawl_button).to_be_visible()
```

### Page Facade

Combines all three layers into a single, easy-to-use interface.

**Example from `customer_page.py`:**
```python
class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = CustomerLocators(page)
        self.actions = CustomerActions(page)
        self.validations = CustomerValidations(page)
```

## 💡 Usage Examples

### Basic Test Structure

```python
from pages.login.login_page import LoginPage
from pages.customer.customer_page import CustomerPage

def test_customer_login_with_new_structure(page: Page):
    # Initialize page objects
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    
    # Actions
    login_page.actions.navigate()
    login_page.actions.click_customer_login()
    
    # Validations
    customer_page.validations.verify_customer_selection_page_loaded()
    
    # More actions
    customer_page.actions.select_user_by_name("Hermoine Granger")
    customer_page.actions.click_login()
    
    # More validations
    customer_page.validations.verify_account_page_loaded()
    customer_page.validations.verify_all_account_buttons_visible()
```

### Using Dynamic Locators

```python
def test_using_dynamic_locators(page: Page):
    login_page = LoginPage(page)
    
    login_page.actions.navigate()
    
    # Use dynamic locator method
    custom_button = login_page.locators.button_by_name("Customer Login")
    custom_button.click()
    
    page.wait_for_url("**/customer")
```

### Deposit Workflow

```python
def test_deposit_with_new_structure(page: Page):
    login_page = LoginPage(page)
    customer_page = CustomerPage(page)
    
    # Login flow
    login_page.actions.navigate()
    login_page.actions.click_customer_login()
    customer_page.actions.select_user_by_name("Hermoine Granger")
    customer_page.actions.click_login()
    
    # Deposit action
    customer_page.actions.perform_deposit("1000")
    
    # Validation
    customer_page.validations.verify_deposit_successful()
```

## 🚀 Key Features

### 1. Dynamic Locators
Similar to TypeScript/JavaScript patterns, you can create parameterized locators:

```python
# In locators file
def button_by_name(self, button_name: str) -> Locator:
    return self.page.get_by_role("button", name=button_name)

def account_info_by_label(self, label: str) -> Locator:
    return self.page.locator(f"text={label}").locator("..").locator("strong")

# Usage in test
button = customer_page.locators.button_by_name("Deposit")
```

### 2. Playwright Built-in Locators
Using Playwright's recommended locators with auto-wait and auto-retry:
- `get_by_role()` - For buttons, links, etc.
- `get_by_text()` - For text content
- `get_by_placeholder()` - For input fields
- `get_by_label()` - For form labels
- `locator()` - For CSS/XPath when needed

### 3. Clear Separation of Concerns
- **Locators** - "What elements exist?"
- **Actions** - "What can I do?"
- **Validations** - "Is it correct?"

### 4. Easy to Extend
Adding new functionality is straightforward:
1. Add locator to `*_locators.py`
2. Add action method to `*_actions.py`
3. Add validation to `*_validations.py`
4. Use in tests via the page facade

## 🔧 Running Tests

```bash
# Run test with new structure
pytest tests/test_new_structure.py -v --headed

# Run specific test
pytest tests/test_new_structure.py::TestNewStructure::test_customer_login_with_new_structure -v

# Run all tests
pytest -v
```

## 📊 Benefits of This Architecture

1. **Maintainability** - UI changes only require updates to locators
2. **Reusability** - Actions and validations can be mixed and matched
3. **Readability** - Tests read like user stories
4. **Scalability** - Easy to add new pages and functionality
5. **Testability** - Each layer can be unit tested
6. **Collaboration** - Clear structure for team development
7. **Type Safety** - Full type hints for IDE support

## 🎓 Best Practices

1. **Keep locators simple** - One locator per element or dynamic pattern
2. **Make actions atomic** - Each action should do one thing well
3. **Validations should be specific** - Clear, focused assertions
4. **Use dynamic locators** - For patterns that repeat with different parameters
5. **Leverage Playwright's built-in locators** - They're more reliable than CSS/XPath
6. **Wait in actions** - Include necessary waits in action methods
7. **Assert in validations** - Keep assertions out of actions

## 🔄 Migration from Old Structure

Old structure:
```python
# Everything in one file
class LoginPage(BasePage):
    @property
    def customer_login_button(self):
        return self.page.get_by_role("button", name="Customer Login")
    
    def click_customer_login(self):
        self.customer_login_button.click()
```

New structure:
```python
# Separated into three files
# locators file
@property
def customer_login_button(self):
    return self.page.get_by_role("button", name="Customer Login")

# actions file
def click_customer_login(self):
    self.locators.customer_login_button.click()

# validations file
def verify_customer_login_button_visible(self):
    expect(self.locators.customer_login_button).to_be_visible()
```

## 📝 Next Steps

1. Create additional page objects for other pages
2. Add more dynamic locators as patterns emerge
3. Build comprehensive test suites using the new structure
4. Add integration with CI/CD pipelines
5. Create custom reporters for better test visibility
