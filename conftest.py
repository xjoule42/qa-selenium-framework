import pytest

from src.core.driver_factory import DriverFactory
from src.core.logger import Logger

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