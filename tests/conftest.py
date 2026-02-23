import pytest
import json
from pathlib import Path

@pytest.fixture
def test_data():
    """Load test data from JSON file"""
    data_file = Path(__file__).parent / "test_data.json"
    with open(data_file, 'r') as f:
        return json.load(f)

@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
