import pytest

from src.pages.login_page import LoginPage

@pytest.mark.smoke
def test_successful_login(driver):
    """
    Verify that a standard user can log in successfully.
    """

    login_page = LoginPage(driver)

    login_page.open()

    assert login_page.is_login_page(), \
    "The login page was not displayed"

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    assert "inventory" in login_page.get_current_url(), \
    "The user was not redirected to the inventory page after login."