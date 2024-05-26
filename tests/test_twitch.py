import pytest
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
from pytest import fixture


@pytest.mark.usefixtures('browser')
def test_twitch_search(browser):
    home_page = TwitchHomePage(browser)
    search_results_page = TwitchSearchResultsPage(browser)
    streamer_page = TwitchStreamerPage(browser)

    home_page.go_to_site()
    home_page.handle_popup_message()
    home_page.search_for("StarCraft II")
    search_results_page.scroll_down(times=2)
    search_results_page.select_first_streamer()
    streamer_page.handle_popup()
    streamer_page.wait_for_stream_to_load()
    streamer_page.take_screenshot("streamer_page.png")
