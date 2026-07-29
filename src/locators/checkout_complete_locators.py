from selenium.webdriver.common.by import By

class CheckoutCompleteLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    BACK_HOME_BUTTON = (By.ID, "back-to-products")