import pytest
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage

from utils.logger import setup_logger

logger = setup_logger(__name__, 'streamer_page.log')


class TestTwitch:

    @pytest.mark.parametrize("query", ["StarCraft II"])
    def test_twitch_search(self, page, query):
        logger.info("Starting test: test_twitch_search")
        # context = await browser.new_context()
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
