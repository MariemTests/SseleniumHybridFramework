import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(time_to_wait=10)
    driver.maximize_window()

    return driver
