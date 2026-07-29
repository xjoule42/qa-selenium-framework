import pytest
import os

from src.pages.cart_page import CartPage
from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage


@pytest.mark.smoke
def test_cart_page(driver):
    """
    Verify that a product added to the cart
    is displayed in the shopping cart page.
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()

    login_page.login(
        os.getenv("STANDARD_USER"),
        os.getenv("STANDARD_PASSWORD"),
    )

    assert inventory_page.is_inventory_page(), (
        "The inventory page was not displayed."
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.open_cart()

    assert cart_page.is_cart_page(), (
        "The cart page was not displayed."
    )

    assert cart_page.get_cart_items_count() == 1, (
        "The cart should contain one product."
    )