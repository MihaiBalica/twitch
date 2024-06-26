"""
Contains the TwitchStreamerPage class, which represents the Twitch streamer page.
"""

from pages.base_page import BasePage
from utils.locators import StreamerPageLocators

class TwitchStreamerPage(BasePage):
    """
    represents the Twitch streamer page.
    """

    def __init__(self, page):
        super().__init__(page)
        self.popup_button_locator = page.locator(StreamerPageLocators.POPUP_BUTTON)
        self.video_container_locator = page.locator(StreamerPageLocators.VIDEO_CONTAINER)

    def handle_popup(self) -> None:
        """
        handles the popup on the streamer page.
        :return: None
        """
        try:
            self.popup_button_locator.wait_for(timeout=5000)
            popup_button = self.popup_button_locator.first
            popup_button.click()
            self.logger.info("Popup was closed.")
        except Exception as e:
            self.logger.error("Error handling popup:", exc_info=e)

    def wait_for_stream_to_load(self) -> None:
        """
        waits for the stream to load on the streamer page.
        :return: None
        """
        try:
            self.video_container_locator.wait_for(timeout=5000)
            self.logger.info("Stream loaded.")
            self.take_screenshot("streamer_shot_stream_loaded.png")
        except Exception as e:
            self.logger.error("Error waiting for stream to load:", exc_info=e)
            self.take_screenshot("streamer_shot_stream_not_loaded.png")

    def take_screenshot(self, filename: str) -> None:
        """
        takes a screenshot of the streamer page.
        :param filename: The filename to save the screenshot as.
        :return: None
        """
        try:
            self.page.screenshot(path=filename)
            self.logger.info(f"Screenshot saved as {filename}.")
        except Exception as e:
            self.logger.error("Error taking screenshot:", exc_info=e)
