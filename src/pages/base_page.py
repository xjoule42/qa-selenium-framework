from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config.config import Config
from src.core.logger import Logger
from src.core.waits import Waits
from selenium.common.exceptions import TimeoutException
from typing import Optional
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
)

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


    def click(self, locator) -> None:
        """
        Click an element with a retry to reduce flaky failures
        in Chrome Headless / CI environments.
        """

        logger.info(f"Clicking element: {locator}")

        last_exception = None

        for attempt in range(2):

            try:
                element = self.wait.until_clickable(locator)

                print(f"Click attempt: {attempt + 1}")
                print("Enabled:", element.is_enabled())
                print("Displayed:", element.is_displayed())

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                print("URL after click:", self.driver.current_url)

                # Si el click fue exitoso, salir.
                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException
            ) as e:

                logger.warning(
                    f"Click failed (attempt {attempt + 1}), retrying..."
                )

                last_exception = e

        # Si ambos intentos fallan, lanzar la excepción original
        raise last_exception

    def type(self, locator, text: str) -> None:
        logger.info(f"Typing into element: {locator}")

        element = self.wait.until_clickable(locator)

        element.click()
        element.clear()

        # Volver a localizar por si el DOM cambió
        element = self.wait.until_clickable(locator)

        element.send_keys(text)

        print("ACTIVE:", self.driver.switch_to.active_element.get_attribute("id"))
        print("CURRENT:", element.get_attribute("id"))
        print("VALUE:", repr(element.get_attribute("value")))

        value = element.get_attribute("value")

        print(f"{locator} -> {repr(value)}")

        assert value == text, (
            f"Input {locator} expected '{text}' but got '{value}'"
        )

    def clear(self, locator) -> None:
        self.wait.until_visible(locator).clear()

    def get_text(self, locator) -> str:
        return self.wait.until_visible(locator).text

    def get_attribute(
            self,
            locator,
            attribute: str
            ) -> Optional[str]:
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