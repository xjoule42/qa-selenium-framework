from pathlib import Path

class ScreenshotManager:

    SCREENSHOT_DIR = Path("reports/screenshots")

    @classmethod
    def save(cls, driver, name: str):
        cls.SCREENSHOT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        driver.save_screenshot(
            str(cls.SCREENSHOT_DIR / f"{name}.png")
        )