import config.settings as settings


class Config:
    """Application configuration."""

    # Environment
    BASE_URL = settings.BASE_URL

    # Browser
    CHROME = settings.CHROME
    FIREFOX = settings.FIREFOX
    EDGE = settings.EDGE

    BROWSER = settings.BROWSER
    HEADLESS = settings.HEADLESS

    # Timeouts
    IMPLICIT_WAIT = settings.IMPLICIT_WAIT
    EXPLICIT_WAIT = settings.EXPLICIT_WAIT
    PAGE_LOAD_TIMEOUT = settings.PAGE_LOAD_TIMEOUT

    # Window
    WINDOW_WIDTH = settings.WINDOW_WIDTH
    WINDOW_HEIGHT = settings.WINDOW_HEIGHT

    # Directories
    PROJECT_ROOT = settings.PROJECT_ROOT
    LOGS_DIR = settings.LOGS_DIR
    REPORTS_DIR = settings.REPORTS_DIR
    HTML_REPORT_DIR = settings.HTML_REPORT_DIR
    SCREENSHOTS_DIR = settings.SCREENSHOTS_DIR
    ALLURE_RESULTS_DIR = settings.ALLURE_RESULTS_DIR

    @classmethod
    def as_dict(cls):
        return {
            "BASE_URL": cls.BASE_URL,
            "BROWSER": cls.BROWSER,
            "HEADLESS": cls.HEADLESS,
            "IMPLICIT_WAIT": cls.IMPLICIT_WAIT,
            "EXPLICIT_WAIT": cls.EXPLICIT_WAIT,
            "PAGE_LOAD_TIMEOUT": cls.PAGE_LOAD_TIMEOUT,
            "WINDOW_WIDTH": cls.WINDOW_WIDTH,
            "WINDOW_HEIGHT": cls.WINDOW_HEIGHT,
        }