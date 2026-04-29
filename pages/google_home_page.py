from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class GoogleHomePage:
    URL = "https://www.google.com"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        return self

    def wait_until_loaded(self):
        self.wait.until(ec.title_contains("Google"))
        return self

    @property
    def title(self):
        return self.driver.title
