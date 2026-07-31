from src.pages.base_page import BasePage
from src.locators.checkout_information_locators import CheckoutInformationLocators
from selenium.common.exceptions import NoSuchElementException
import time


class CheckoutInformationPage(BasePage):

    def is_checkout_information_page(self) -> bool:
        return (
            self.is_visible(CheckoutInformationLocators.PAGE_TITLE)
            and self.has_url("checkout-step-one.html")
        )

    def fill_first_name(self, first_name: str) -> None:
        self.type(
            CheckoutInformationLocators.FIRST_NAME_INPUT,
            first_name
        )

    def fill_last_name(self, last_name: str) -> None:
        self.type(
            CheckoutInformationLocators.LAST_NAME_INPUT,
            last_name
        )

    def fill_postal_code(self, postal_code: str) -> None:
        self.type(
            CheckoutInformationLocators.POSTAL_CODE_INPUT,
            postal_code
        )

    def continue_checkout(self) -> None:

        self.click(
            CheckoutInformationLocators.CONTINUE_BUTTON
        )

        

        try:
            error = self.driver.find_element(
                *CheckoutInformationLocators.ERROR_MESSAGE
            )

            print(f"Checkout error: {error.text}")

        except NoSuchElementException:
            print("No checkout error found.")

        self.wait.until_url_contains(
            "checkout-step-two.html"
        )
    def cancel_checkout(self) -> None:
        self.click(
            CheckoutInformationLocators.CANCEL_BUTTON
        )

    def fill_checkout_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:

        time.sleep(1)

        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)

    def get_checkout_error(self):

        if self.is_visible(
            CheckoutInformationLocators.ERROR_MESSAGE
        ):
            return self.get_text(
                CheckoutInformationLocators.ERROR_MESSAGE
            )

        return None