import os

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_information_page import CheckoutInformationPage
from src.pages.checkout_overview_page import CheckoutOverviewPage
from src.pages.checkout_complete_page import CheckoutCompletePage


def test_complete_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckoutInformationPage(driver)
    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

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

    assert cart_page.is_cart_page(),(
        "Cart page should be displayed."
    )

    # assert False, "Intentional failure"

    cart_page.click_checkout()

    assert checkout_information_page.is_checkout_information_page(), (
        "Checkout information page should be displayed."
    )

    checkout_information_page.fill_checkout_information(
        "Julio",
        "Soto",
        "99000",
    )

    checkout_information_page.continue_checkout()

    assert checkout_overview_page.is_checkout_overview_page(), (
        "Checkout overview page should be displayed."
    )

    checkout_overview_page.finish_checkout()

    assert checkout_complete_page.is_checkout_complete_page(), (
        "Checkout Complete page should be displayed."
    )

    assert (
        checkout_complete_page.get_complete_header()
        == "Thank you for your order!"
    ),(
        "Success message should be displayed after completing the purchase."
    )

    checkout_complete_page.click_back_home()

    assert inventory_page.is_inventory_page(), (
        "User should return to Inventory page after clicking Back Home."
    )