import pytest

from src.core.driver_factory import DriverFactory
from src.core.logger import Logger
from src.utils.screenshot import ScreenshotManager
from datetime import datetime
logger = Logger.get_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Create a WebDriver instance for each test.
    """

    logger.info("Starting browser")

    driver = DriverFactory.create_driver()

    yield driver

    logger.info("Closing browser")

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Save a screenshot automatically whenever a test fails.
    """

    outcome = yield
    report = outcome.get_result()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            ScreenshotManager.save(driver, f"{item.name}_{timestamp}")