from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config import Config
from src.core.logger import Logger

logger = Logger.get_logger(__name__)


class DriverFactory:
    """
    Factory responsible for creating configured Selenium WebDriver instances.
    """

    @staticmethod
    def create_driver() -> WebDriver:
        """
        Create and configure a WebDriver instance based on project settings.
        """

        browser = Config.BROWSER.lower()

        logger.info(
            f"Initializing {browser.capitalize()} browser "
            f"(headless={Config.HEADLESS})"
        )

        if browser == Config.CHROME:
            driver = DriverFactory._create_chrome_driver()

        elif browser == Config.FIREFOX:
            driver = DriverFactory._create_firefox_driver()

        elif browser == Config.EDGE:
            driver = DriverFactory._create_edge_driver()

        else:
            supported = (
                Config.CHROME,
                Config.FIREFOX,
                Config.EDGE,
            )

            logger.error(f"Unsupported browser: {browser}")

            raise ValueError(
                f"Unsupported browser '{browser}'. "
                f"Supported browsers: {', '.join(supported)}."
            )

        DriverFactory._configure_driver(driver)

        logger.info(
            f"Browser initialized successfully "
            f"({Config.WINDOW_WIDTH}x{Config.WINDOW_HEIGHT})"
        )

        return driver

    @staticmethod
    def _configure_driver(driver: WebDriver) -> None:
        """
        Apply common configuration to all browsers.
        """

        driver.set_window_size(
            Config.WINDOW_WIDTH,
            Config.WINDOW_HEIGHT,
        )

        driver.implicitly_wait(
            Config.IMPLICIT_WAIT
        )

        driver.set_page_load_timeout(
            Config.PAGE_LOAD_TIMEOUT
        )

    # ------------------------------------------------------------------
    # Browser creation
    # ------------------------------------------------------------------

    @staticmethod
    def _create_chrome_driver() -> WebDriver:
        return webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            ),
            options=DriverFactory._create_chrome_options(),
        )

    @staticmethod
    def _create_firefox_driver() -> WebDriver:
        return webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()
            ),
            options=DriverFactory._create_firefox_options(),
        )

    @staticmethod
    def _create_edge_driver() -> WebDriver:
        return webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            ),
            options=DriverFactory._create_edge_options(),
        )

    # ------------------------------------------------------------------
    # Browser options
    # ------------------------------------------------------------------

    @staticmethod
    def _apply_chromium_options(options) -> None:
        """
        Apply common Chromium options.
        """

        if Config.HEADLESS:
                
                options.add_argument("--headless=new")

        options.add_argument("--window-size=1920,1080")

        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")

        # Required for GitHub Actions / Linux CI
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")


        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
            },
        )

        options.add_experimental_option(
            "excludeSwitches",
            ["enable-automation"]
        )


    @staticmethod
    def _create_chrome_options() -> ChromeOptions:
        options = ChromeOptions()
        DriverFactory._apply_chromium_options(options)
        return options

    @staticmethod
    def _create_edge_options() -> EdgeOptions:
        options = EdgeOptions()
        DriverFactory._apply_chromium_options(options)
        return options

    @staticmethod
    def _create_firefox_options() -> FirefoxOptions:
        options = FirefoxOptions()

        if Config.HEADLESS:
            options.add_argument("-headless")

        return options