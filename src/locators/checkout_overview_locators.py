from selenium.webdriver.common.by import By


class CheckoutOverviewLocators:

    PAGE_TITLE = (By.CSS_SELECTOR, ".title")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")