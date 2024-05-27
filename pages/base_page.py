from utils.config import Config
from utils.logger import setup_logger


class BasePage:

    def __init__(self, page):
        self.page = page
        self.URL = Config.URL
        self.logger = setup_logger(self.__class__.__name__, 'streamer_page.log')

    def go_to_site(self, url):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)
