from src.pages.base_page import BasePage
from src.locators.cart_locators import CartLocators


class CartPage(BasePage):

    def is_cart_page(self) -> bool:
        return(
            self.has_url(CartLocators.PAGE_URL)
            and self.is_visible(CartLocators.PAGE_TITLE)
        )

    def get_cart_items(self):
        return self.find_elements(
            CartLocators.CART_ITEMS
        )

    def get_cart_items_count(self) -> int:
        return self.get_elements_count(
            CartLocators.CART_ITEMS
        )

    def click_checkout(self):
        self.click(
            CartLocators.CHECKOUT_BUTTON
        )

    def continue_shopping(self):
        self.click(
            CartLocators.CONTINUE_SHOPPING_BUTTON
        )