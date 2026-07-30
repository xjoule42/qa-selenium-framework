from src.pages.base_page import BasePage
from src.locators.checkout_overview_locators import (
    CheckoutOverviewLocators,
)


class CheckoutOverviewPage(BasePage):

    def is_checkout_overview_page(self) -> bool:
        visible = self.is_visible(
            CheckoutOverviewLocators.PAGE_TITLE
        )

        url = self.has_url("checkout-step-two.html")

        print(f"VISIBLE = {visible}")
        print(f"URL = {url}")

        return visible and url

    def get_cart_items_count(self) -> int:
        return self.get_elements_count(
            CheckoutOverviewLocators.CART_ITEMS
        )

    def get_item_total(self) -> str:
        return self.get_text(
            CheckoutOverviewLocators.ITEM_TOTAL
        )

    def get_tax(self) -> str:
        return self.get_text(
            CheckoutOverviewLocators.TAX
        )

    def get_total(self) -> str:
        return self.get_text(
            CheckoutOverviewLocators.TOTAL
        )

    def finish_checkout(self) -> None:
        self.click(
            CheckoutOverviewLocators.FINISH_BUTTON
        )
        self.wait.until_url_contains(
            "checkout-complete.html"
        )

    def cancel_checkout(self) -> None:
        self.click(
            CheckoutOverviewLocators.CANCEL_BUTTON
        )