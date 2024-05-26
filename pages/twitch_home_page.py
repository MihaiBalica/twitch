from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import setup_logger
from utils.config import Config

logger = setup_logger(__name__, 'streamer_page.log')


class TwitchHomePage:
    URL = Config.URL

    def __init__(self, browser):
        self.browser = browser
        self.search_icon_locator = (By.XPATH, "//a[@href='/search' and @aria-label='Search']")
        self.search_input_locator = (By.XPATH, "//input[@type='search' and @placeholder='Search...']")

    def handle_popup_message(self):
        try:
            # Wait for the button to be visible and click it if it appears
            close_button = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//button[.//div[contains(text(),'Close')]]"))
            )
            close_button.click()
            logger.info("Popup closed successfully.")
        except (TimeoutException, NoSuchElementException):
            logger.info("No popup appeared.")

    def go_to_site(self):
        logger.info("Navigating to url: {}".format(self.URL))
        self.browser.get(self.URL)

    def search_for(self, query):
        search_icon = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.search_icon_locator)
        )
        logger.info("Search button is available!")
        search_icon.click()
        logger.info("Search button clicked!")
        search_input = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.search_input_locator)
        )
        logger.info("Search input is available!")
        logger.info("Introducing search text '{}' into search input field".format(query))
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)
        logger.info("Search text entered and hit ENTER")
