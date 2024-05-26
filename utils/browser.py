from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", {
        "deviceName": "Nexus 5"
    })
    # chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
    chrome_options.add_argument("--window-size=375,812")  # Set window size for mobile emulation
    driver = webdriver.Chrome(options=chrome_options)
    return driver
