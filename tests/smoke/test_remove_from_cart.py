import pytest

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_remove_product_from_cart(driver):
    """
    Verify that a product can be removed from the shopping cart.
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()

    login_page.login(
        username="standard_user",
        password="secret_sauce",
    )

    assert inventory_page.is_inventory_page(), (
        "The inventory page was not displayed."
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert inventory_page.get_cart_badge_count() == 1, (
        "The shopping cart badge should display one product."
    )

    inventory_page.remove_product_from_cart(
        "Sauce Labs Backpack"
    )

    assert inventory_page.get_cart_badge_count() == 0, (
        "The shopping cart should be empty."
    )