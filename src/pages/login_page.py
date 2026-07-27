from src.locators.login_locators import LoginLocators
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the SauceDemo login page.
    """

    def open(self) -> None:
        """
        Open the login page.
        """

        super().open()

    def login(self, username: str, password: str) -> None:
        """
        Log in with the provided credentials.
        """

        self.type(LoginLocators.USERNAME_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """
        Return the login error message.
        """

        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_login_page(self) -> bool:
        """
        Verify that the login page is displayed.
        """

        return (
            self.is_visible(LoginLocators.USERNAME_INPUT)
            and self.is_visible(LoginLocators.PASSWORD_INPUT)
            and self.is_visible(LoginLocators.LOGIN_BUTTON)
        )