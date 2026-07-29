import os

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_information_page import CheckoutInformationPage


def test_checkout_information(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_information_page = CheckoutInformationPage(driver)

    login_page.open()

    login_page.login(
        os.getenv("STANDARD_USERNAME"),
        os.getenv("STANDARD_PASSWORD"),
    )

    assert inventory_page.is_inventory_page(),(
        "Inventory page should be displayed after login."
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert inventory_page.get_cart_badge_count() == 1,(
        "Cart badge should be display one item."
    )

    inventory_page.open_cart()

    assert cart_page.is_cart_page(), (
        "Cart page should be displayed"
    )

    cart_page.click_checkout()

    assert checkout_information_page.is_checkout_information_page(),(
        "Checkout Information page should be displayed"
    )



    checkout_information_page.fill_checkout_information(
        "Julio",
        "Soto",
        "99000",
    )

    checkout_information_page.continue_checkout()
    print(driver.current_url)
    assert checkout_information_page.has_url(
        "checkout-step-two.html"
    ), (
        "User should be redirected to Checkout Overview page."
    )