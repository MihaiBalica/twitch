"""
test cases for Twitch functionalities.
"""

import pytest
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
from utils.logger import setup_logger

logger = setup_logger(__name__, 'streamer_page.log')


class TestTwitch:
    """
    Test cases for Twitch functionalities.
    """

    @pytest.mark.parametrize("query", ["StarCraft II"])
    def test_twitch_search(self, page, query):
        """
        Test case to search for a specific game on Twitch.

        :param page: Playwright page object representing the browser page.
        :param query: The search query to be performed.
        """
        logger.info("Starting test: test_twitch_search")

        home_page = TwitchHomePage(page)
        search_results_page = TwitchSearchResultsPage(page)
        streamer_page = TwitchStreamerPage(page)

        home_page.go_to_site()
        home_page.handle_popup_message()
        home_page.search_for(query)
        search_results_page.scroll_down(times=2)
        search_results_page.select_first_streamer()
        streamer_page.handle_popup()
        streamer_page.wait_for_stream_to_load()
        streamer_page.take_screenshot("streamer_page.png")

        logger.info("Test completed: test_twitch_search")
