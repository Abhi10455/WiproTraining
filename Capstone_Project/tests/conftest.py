import pytest
import configparser
import os
from utilities.driver_factory import get_driver
from utilities.logger import get_logger

logger = get_logger()


#Add CLI option for browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,  # fallback to config.ini if not provided
        help="Browser to run tests: chrome, firefox, edge"
    )


#Fixture to set up driver
@pytest.fixture(scope="function")
def setup(request):
    cli_browser = request.config.getoption("--browser")

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config/config.ini"))

    if cli_browser:
        config["DEFAULT"]["browser"] = cli_browser.lower()

    browser_name = cli_browser if cli_browser else config["DEFAULT"]["browser"]
    browser_name = browser_name.lower()

    logger.info(f"Browser Setup Started: {browser_name}")

    driver = get_driver(browser_name)

    base_url = config["DEFAULT"]["base_url"]
    driver.get(base_url)

    yield driver

    logger.info("Browser Teardown Started")
    driver.quit()
    logger.info("Browser Closed Successfully\n")

