import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import setup_logger

logger = setup_logger(__name__, 'streamer_page.log')


class TwitchStreamerPage:
    def __init__(self, browser):
        self.browser = browser
        self.popup_button = (By.XPATH, "//button//div[contains(text(), 'Start Watching')]")
        self.video_container_locator = (By.XPATH, "//video[contains(@src, 'blob:https://m.twitch.tv/')]")

    def handle_popup(self):
        try:
            close_button = WebDriverWait(self.browser, 3).until(
                EC.element_to_be_clickable(self.popup_button)
            )
            close_button.click()
        except (TimeoutException, NoSuchElementException):
            logger.info("No popup appeared.")

    def is_video_playing(self):
        # Execute JavaScript to check if the video element is playing
        script = "return arguments[0].paused === false && arguments[0].ended === false"
        video_element = self.browser.find_element(By.TAG_NAME, "video")
        return self.browser.execute_script(script, video_element)

    def wait_for_stream_to_load(self):
        logger.info("Waiting for stream to load...")
        WebDriverWait(self.browser, 15).until(
            EC.presence_of_element_located(self.video_container_locator)
        )
        retry = 5
        while not self.is_video_playing() and retry > 0:
            logger.info("Waiting for stream to load...")
            retry -= 1
        if self.is_video_playing():
            logger.info("Stream loaded.")
        else:
            logger.info("Stream not loaded.")
            self.take_screenshot("streamer_shot__stream_not_loaded.png")

    def take_screenshot(self, file_path):
        self.browser.save_screenshot(file_path)
