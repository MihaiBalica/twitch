class HomePageLocators:
    SEARCH_ICON = "//a[@href='/search' and @aria-label='Search']"
    SEARCH_INPUT = "//input[@type='search' and @placeholder='Search...']"
    POPUP_CLOSE_BUTTON = "//button[.//div[text()='Close']]"


class StreamerPageLocators:
    POPUP_BUTTON = "//button//div[contains(text(), 'Start Watching')]"
    VIDEO_CONTAINER = "//video[contains(@src, 'blob:https://m.twitch.tv/')]"


class SearchResultsPageLocators:
    SEARCH_RESULT = "(//div//a[contains(@class, 'tw-link')])[2]"
