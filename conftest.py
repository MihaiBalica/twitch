import pytest
from utils.browser import get_chrome_driver
import os
from utils.logger import setup_logger

logger = setup_logger(__name__, 'streamer_page.log')

@pytest.fixture
def browser(request):
    driver = get_chrome_driver()
    driver.implicitly_wait(10)

    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = f'screenshots/{request.node.name}.png'
        try:
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved to {screenshot_path}")
        except Exception as e:
            logger.info(f"Could not take screenshot: {e}")

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set an attribute on the item for each phase of a call, so we can access it in fixtures
    setattr(item, "rep_" + rep.when, rep)