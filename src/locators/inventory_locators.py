from selenium.webdriver.common.by import By

class InventoryLocators:
    """
    Locators for the SauceDemo inventory page.
    """

    PAGE_TITLE = (By.CLASS_NAME, "title")

    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    