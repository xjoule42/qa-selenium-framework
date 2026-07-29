from selenium.webdriver.common.by import By

class CartLocators:

    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    CHECKOUT_BUTTON = (By.ID, "checkout")

    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    PAGE_URL = "cart.html"