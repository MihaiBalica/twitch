"""
Configuration file for pytest.
"""
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """
    browser session fixture
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, executable_path="/opt/google/chrome/chrome")
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """
    context fixture
    :param browser:
    :return:
    """
    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        record_video_dir="videos/",
        viewport={"width": 375, "height": 812},
        is_mobile=True,
        locale="en-US",
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """
    Page fixture
    :param context:
    :return:
    """
    page = context.new_page()
    yield page
    page.close()
