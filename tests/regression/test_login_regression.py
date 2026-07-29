import pytest

from src.pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        pytest.param(
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
            id="invalid_password",
        ),
        pytest.param(
            "wrong_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
            id="invalid_username",
        ),
        pytest.param(
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
            id="locked_user",
        ),
        pytest.param(
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
            id="empty_username",
        ),
        pytest.param(
            "standard_user",
            "",
            "Epic sadface: Password is required",
            id="empty_password",
        ),
        pytest.param(
            "",
            "",
            "Epic sadface: Username is required",
            id="empty_credentials",
        ),
    ],
)
def test_unsuccessful_login(driver, username, password, expected_error):
    """
    Verify that invalid login attempts display the correct error message.
    """

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username, password)

    assert login_page.get_error_message() == expected_error