import pytest
from selene import browser


@pytest.fixture
def driver():
    browser.config.window_width = 1024
    browser.config.window_heigh = 768
    browser.open('https://google.com/ncr')

    yield browser

    browser.quit()
