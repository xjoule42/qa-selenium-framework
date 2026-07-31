from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config.config import Config
from src.core.logger import Logger
from src.core.waits import Waits
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    )
from typing import Optional


logger = Logger.get_logger(__name__)


class BasePage:
    """
    Base class for all Page Objects.
    """

    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.wait = Waits(driver)

    # ---------------------------------------------------------
    # Navigation
    # ---------------------------------------------------------

    def open(self, url: str = "") -> None:
        """
        Open a page.
        """

        target = Config.BASE_URL + url

        logger.info(f"Opening: {target}")

        self.driver.get(target)

    # ---------------------------------------------------------
    # Elements
    # ---------------------------------------------------------

    def find_element(self, locator) -> WebElement:
        """
        Find an Element.
        """
        return self.wait.until_present(locator)

    def find_elements(self, locator):
        """
        Find all elements matching the given locator.
        """

        logger.info(f"Finding elements: {locator}")
        self.wait.until_present(locator)
        return self.driver.find_elements(*locator)

    def get_elements_count(self, locator) -> int:
        """
        Return the number of elements matching the locator.
        """

        return len(self.find_elements(locator))


    def click(self, locator):
        element = self.wait.until_clickable(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )
        
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        
    def type(self, locator, text: str, verify: bool = True) -> None:
        """
        Clear an input and type text into it.
        """

        logger.info(f"Typing '{text}' into {locator}")

        element = self.wait.until_clickable(locator)

        element.clear()

        print("AFTER CLEAR:", element.get_attribute("value"))

        element.send_keys(text)

        print("AFTER SEND_KEYS:", element.get_attribute("value"))

        current = element.get_attribute("value")

        logger.info(f"Current input value: '{current}'")

        if current == text:
            return

        logger.error(
            f"Unable to type '{text}' after retries."
        )
        
        raise AssertionError(
            f"Input value mismatch. Expected '{text}', got '{current}'"
        )

    def clear(self, locator) -> None:
        """
        Clear an input field.
        """

        logger.info(f"Clearing element: {locator}")

        self.wait.until_clickable(locator).clear()

    def get_text(self, locator) -> str:
        """
        Return visible text.
        """
        return self.wait.until_visible(locator).text

    def get_attribute(
            self,
            locator,
            attribute: str
            ) -> Optional[str]:
        """
        Return an attribute from an element.
        """
        return self.wait.until_visible(locator).get_attribute(attribute)

    # ---------------------------------------------------------
    # State
    # ---------------------------------------------------------

    def is_visible(self, locator) -> bool:

        try:
            self.wait.until_visible(locator)
            return True

        except TimeoutException:
            return False

    def is_enabled(self, locator) -> bool:
        return self.wait.until_visible(locator).is_enabled()

    def is_selected(self, locator) -> bool:
        return self.wait.until_visible(locator).is_selected()

    # ---------------------------------------------------------
    # Mouse
    # ---------------------------------------------------------

    def hover(self, locator) -> None:

        element = self.wait.until_visible(locator)

        ActionChains(self.driver)\
            .move_to_element(element)\
            .perform()

    # ---------------------------------------------------------
    # Browser
    # ---------------------------------------------------------

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url

    def refresh(self) -> None:
        self.driver.refresh()

    def back(self) -> None:
        self.driver.back()

    def forward(self) -> None:
        self.driver.forward()

    def get_page_source(self) -> str:
        """
        Return the current page source.
        """

        return self.driver.page_source

    def has_url(self, expected_url: str) -> bool:
        current = self.driver.current_url

        print(f"EXPECTED URL PART: {expected_url}")
        print(f"CURRENT URL: {current}")

        logger.info(f"Validating URL contains: {expected_url}")

        return expected_url in current