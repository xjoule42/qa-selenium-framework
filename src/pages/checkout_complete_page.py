from src.pages.base_page import BasePage
from src.locators.checkout_complete_locators import (
    CheckoutCompleteLocators,
)


class CheckoutCompletePage(BasePage):

    def is_checkout_complete_page(self) -> bool:
        return(
            self.is_visible(
                CheckoutCompleteLocators.PAGE_TITLE
            )
            and self.has_url("checkout-complete.html")
        )

    def get_complete_header(self) -> str:
        return self.get_text(
            CheckoutCompleteLocators.COMPLETE_HEADER
        )

    def get_complete_message(self) -> str:
        return self.get_text(
            CheckoutCompleteLocators.COMPLETE_TEXT
        )

    def click_back_home(self) -> None:
        self.click(
            CheckoutCompleteLocators.BACK_HOME_BUTTON
        )
        