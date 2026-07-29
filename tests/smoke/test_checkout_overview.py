import os

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_information_page import CheckoutInformationPage
from src.pages.checkout_overview_page import CheckoutOverviewPage


def test_checkout_overview(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckoutInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)

    login_page.open()

    login_page.login(
        os.getenv("STANDARD_USERNAME"),
        os.getenv("STANDARD_PASSWORD"),
    )

    assert inventory_page.is_inventory_page(), (
        "Inventory page should be displayed after login."
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.open_cart()

    assert cart_page.is_cart_page(), (
        "Cart page should be displayed."
    )

    cart_page.click_checkout()

    assert checkout_information_page.is_checkout_information_page(), (
        "Checkout Information page should be displayed."
    )

    checkout_information_page.fill_checkout_information(
        "Julio",
        "Soto",
        "99000",
    )

    checkout_information_page.continue_checkout()

    assert checkout_overview_page.is_checkout_overview_page(), (
        "Checkout Overview page should be displayed."
    )

    assert checkout_overview_page.get_cart_items_count() == 1, (
        "Checkout should contain one product."
    )

    assert "Item total:" in checkout_overview_page.get_item_total(), (
        "Item total should be displayed."
    )

    assert "Tax:" in checkout_overview_page.get_tax(), (
        "Tax should be displayed."
    )

    assert "Total:" in checkout_overview_page.get_total(), (
        "Total should be displayed."
    )