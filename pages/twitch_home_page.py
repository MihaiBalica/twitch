"""
Twitch Home Page
"""
from pages.base_page import BasePage
from utils.locators import HomePageLocators
from playwright.sync_api import TimeoutError  # Assuming using sync waits


class TwitchHomePage(BasePage):
    """
    class for twitch_home_page page
    """
    def __init__(self, page):
        super().__init__(page)
        self.search_icon_locator = page.locator(HomePageLocators.SEARCH_ICON)
        self.search_input_locator = page.locator(HomePageLocators.SEARCH_INPUT)
        self.popup_close_button_locator = page.locator(HomePageLocators.POPUP_CLOSE_BUTTON)

    def handle_popup_message(self) -> None:
        """
        this handles the popup message, if it appears
        :return:
        """
        try:
            self.popup_close_button_locator.wait_for(timeout=5000)
            popup_close_button = self.popup_close_button_locator.first  # Extract element handle
            popup_close_button.click()  # Click on the element handle
            self.logger.info("Popup closed successfully.")
        except TimeoutError:
            self.logger.info("No popup appeared within the timeout.")
        except Exception as e:
            self.logger.error("Error handling popup message:", exc_info=e)

    def go_to_site(self) -> None:
        """
        this will navigate to the site
        :return:
        """
        self.logger.info("Navigating to url: {}".format(self.url))
        super().go_to_site()  # Assuming inherited implementation

    def search_for(self, query) -> None:
        """
        this will perform the search for a query string
        :param query: the string to search for
        :return:
        """
        try:
            self.search_icon_locator.wait_for(timeout=5000)
            search_icon = self.search_icon_locator.first
            self.logger.info("Search button available.")
            search_icon.click()  # Click on the element handle
            self.logger.info("Search button clicked!")

            search_input = self.search_input_locator.wait_for(timeout=5000)
            search_input = self.search_input_locator.first
            self.logger.info("Search input is available!")

            self.logger.info(f"Introducing search text '{query}' into search input field")
            search_input.fill(query)  # Fill the search input field

            search_input.press("Enter")  # Press Enter key
            self.logger.info("Search text entered and hit ENTER")
        except Exception as e:
            self.logger.error("Error occurred during search:", exc_info=e)
