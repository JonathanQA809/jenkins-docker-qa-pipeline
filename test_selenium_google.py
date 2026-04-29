
from pages.google_home_page import GoogleHomePage


def test_google_title(driver):
    google_home_page = GoogleHomePage(driver).open().wait_until_loaded()

    assert "Google" in google_home_page.title
