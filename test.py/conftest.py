import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium .webdriver.edge.service import Service as EdgeServise
from webdriver_manager.microsoft import EdgeChromiumDriverManager



# @pytest.fixture(params=["chrome", "edge"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        my_driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeServise(EdgeChromiumDriverManager().install())
        my_driver = webdriver.Edge(service=service)
    else:
        TypeError(f"the browser should be either chrome or edge. but it is '{browser}'")
    
    yield my_driver
    my_driver.quit


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to execute test('chrome' or 'edge')")