"""
class for loading environment configuration
"""
import os
from dotenv import load_dotenv


class Config:
    """
    class for loading environment configuration
    """
    load_dotenv()
    URL = os.getenv("URL", "https://m.twitch.tv")
