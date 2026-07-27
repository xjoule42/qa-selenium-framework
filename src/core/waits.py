from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config
from src.core.logger import Logger

logger = Logger.get_logger(__name__)


class Waits:
    """
    Explicit wait helper for Selenium WebDriver.
    """

    def __init__(self, driver: WebDriver):
        """
        Initialize the wait helper.

        Args:
            driver: Selenium WebDriver instance.
        """

        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            Config.EXPLICIT_WAIT
        )

    # ---------------------------------------------------------
    # Element waits
    # ---------------------------------------------------------

    def until_present(self, locator) -> WebElement:
        logger.info(f"Waiting for element to be present: {locator}")

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def until_visible(self, locator) -> WebElement:
        logger.info(f"Waiting for element to be visible: {locator}")

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def until_clickable(self, locator) -> WebElement:
        logger.info(f"Waiting for element to be clickable: {locator}")

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def until_invisible(self, locator) -> bool:
        logger.info(f"Waiting for element to disappear: {locator}")

        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    # ---------------------------------------------------------
    # Page waits
    # ---------------------------------------------------------

    def until_title(self, title: str) -> bool:
        logger.info(f"Waiting for title: '{title}'")

        return self.wait.until(
            EC.title_is(title)
        )

    def until_title_contains(self, text: str) -> bool:
        logger.info(f"Waiting for title to contain: '{text}'")

        return self.wait.until(
            EC.title_contains(text)
        )

    def until_url(self, url: str) -> bool:
        logger.info(f"Waiting for URL: '{url}'")

        return self.wait.until(
            EC.url_to_be(url)
        )

    def until_url_contains(self, text: str) -> bool:
        logger.info(f"Waiting for URL to contain: '{text}'")

        return self.wait.until(
            EC.url_contains(text)
        )

    # ---------------------------------------------------------
    # Browser waits
    # ---------------------------------------------------------

    def until_alert(self):
        logger.info("Waiting for alert")

        return self.wait.until(
            EC.alert_is_present()
        )

    def until_frame(self, locator) -> bool:
        logger.info(f"Waiting for frame: {locator}")

        return self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )