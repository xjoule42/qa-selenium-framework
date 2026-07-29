import pytest
import os

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage

@pytest.mark.smoke
def test_inventory_page_loads_successfully(driver):
    """
    Verify that the inventroy page loads successfully after login.
    """

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()

    login_page.login(
        os.getenv("STANDARD_USER"),
        os.getenv("STANDARD_PASSWORD"),
    )

    assert inventory_page.is_inventory_page(),(
        "The inventory page was not displayed."
    )

    assert inventory_page.get_products_count() > 0, (
        "No products were displayed on the inventory page."
    )

    assert inventory_page.get_cart_badge_count() == 0, (
        "The Shopping cart should be empty."
    )