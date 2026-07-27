from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# --------------------------------------------------------------------
# Project
# --------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------
# Browser
# --------------------------------------------------------------------

CHROME = "chrome"
FIREFOX = "firefox"
EDGE = "edge"

BROWSER = os.getenv("BROWSER", CHROME)
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

# --------------------------------------------------------------------
# Environment
# --------------------------------------------------------------------

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com/"
)

# --------------------------------------------------------------------
# Timeouts
# --------------------------------------------------------------------

IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 10
PAGE_LOAD_TIMEOUT = 30

# --------------------------------------------------------------------
# Window
# --------------------------------------------------------------------

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# --------------------------------------------------------------------
# Directories
# --------------------------------------------------------------------

LOGS_DIR = PROJECT_ROOT / "logs"

REPORTS_DIR = PROJECT_ROOT / "reports"
HTML_REPORT_DIR = REPORTS_DIR / "html"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
ALLURE_RESULTS_DIR = REPORTS_DIR / "allure-results"

for directory in (
    LOGS_DIR,
    HTML_REPORT_DIR,
    SCREENSHOTS_DIR,
    ALLURE_RESULTS_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)