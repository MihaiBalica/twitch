"""
This module provides the base class for all pages.
"""
from utils.config import Config
from utils.logger import setup_logger


class BasePage:
    """
    this is the base class for all pages.
    """

    def __init__(self, page):
        self.page = page
        self.url = Config.URL
        self.logger = setup_logger(self.__class__.__name__, 'streamer_page.log')

    def go_to_site(self) -> None:
        """
        navigate to the site
        """
        self.logger.info(f"Navigating to {self.url}")
        self.page.goto(self.url)
