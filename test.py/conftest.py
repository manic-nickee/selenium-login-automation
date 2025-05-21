import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    my_driver = webdriver.Chrome(service=service)
    yield my_driver
    my_driver.quit