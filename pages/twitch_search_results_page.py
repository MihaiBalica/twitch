"""
Twitch search results page
"""

from pages.base_page import BasePage
from utils.locators import SearchResultsPageLocators

class TwitchSearchResultsPage(BasePage):
    """
    Represents the Twitch search results page.
    """

    def __init__(self, page):
        super().__init__(page)
        self.search_result_locator = page.locator(SearchResultsPageLocators.SEARCH_RESULT)

    def scroll_down(self, times=2) -> None:
        """
        scrolls down the page for a specified number of times.
        :param times: The number of times to scroll down the page. Default is 2.
        :return: None
        """
        for _ in range(times):
            try:
                self.logger.info("Scrolling down")
                self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                self.page.wait_for_timeout(2000)
            except Exception as e:
                self.logger.error("Error occurred while scrolling down:", exc_info=e)

    def select_first_streamer(self) -> None:
        """
        selects the first streamer from the search results.
        :return: None
        """
        try:
            self.search_result_locator.wait_for(timeout=5000)
            first_streamer = self.search_result_locator.nth(0)
            first_streamer.click()
            self.logger.info("Selected first streamer")
        except Exception as e:
            self.logger.error("Error selecting first streamer:", exc_info=e)
