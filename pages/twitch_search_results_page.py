from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TwitchSearchResultsPage:
    def __init__(self, browser):
        self.browser = browser
        self.search_result_locator = (By.XPATH, "//div//a[contains(@class, 'tw-link')]")

    def scroll_down(self, times=2):
        for _ in range(times):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    def select_first_streamer(self):
        streamers = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.search_result_locator)
        )
        streamers[1].click()
