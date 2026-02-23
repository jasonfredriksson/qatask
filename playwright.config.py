# Playwright configuration for pytest-playwright
# This enables Playwright's built-in features like screenshots, videos, and traces

import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context with viewport and other settings"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": "test-results/videos",
        "record_video_size": {"width": 1920, "height": 1080},
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser launch arguments"""
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 0,
    }

@pytest.fixture(scope="function", autouse=True)
def context(context):
    """Enable tracing for all tests"""
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="test-results/trace.zip")
