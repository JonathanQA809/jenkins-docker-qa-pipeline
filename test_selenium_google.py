
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_google_title():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()