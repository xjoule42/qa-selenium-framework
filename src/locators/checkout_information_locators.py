from selenium.webdriver.common.by import By

class CheckoutInformationLocators:
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")