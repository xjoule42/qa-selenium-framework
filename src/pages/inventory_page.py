from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from src.locators.inventory_locators import InventoryLocators
from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for the SauceDemo inventory page.
    """

    def is_inventory_page(self) -> bool:
        """
        Verify that the inventory page is displayed.
        """

        return self.is_visible(InventoryLocators.PAGE_TITLE)

    def get_products(self) -> list:
        """
        Return all available products.
        """

        return self.driver.find_elements(
            InventoryLocators.PRODUCT_ITEMS
            )

    def get_products_count(self) -> int:
        return self.get_elements_count(
            InventoryLocators.PRODUCT_ITEMS
        )

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Add a product to the shopping cart.
        """

        locator = self._build_product_button_locator(
            product_name,
            action="add-to-cart",
        )

        self.click(locator)

   # def is_product_in_cart(self, product_name: str) -> bool:
    #    """
     #   Verify that the product is currently in the cart.
      #  """
       # assert cart_page.is_product_in_cart(
        #    "Sauce Labs Backpack"
        #)


    def remove_product_from_cart(self, product_name: str) -> None:
        """
        Remove a product from the shopping cart.
        """

        locator = self._build_product_button_locator(
            product_name,
            action="remove",
        )

        self.click(locator)

    def open_cart(self) -> None:
        """
        Open the shopping cart.
        """

        self.click(InventoryLocators.SHOPPING_CART_LINK)
        self.wait.until_url_contains("cart.html")

    def get_cart_badge_count(self) -> int:
        """
        Return the number of products in the cart.
        """

        try:
            return int(
                self.get_text(
                    InventoryLocators.SHOPPING_CART_BADGE
                )
            )
        except TimeoutException:
            return 0

    @staticmethod
    def _build_product_button_locator(
        product_name: str,
        action: str,
    ) -> tuple[str, str]:
        """
        Build the locator for an Add/Remove button.
        """

        product_id = (
            product_name
            .lower()
            .replace(" ", "-")
        )

        return (
            By.ID,
            f"{action}-{product_id}",
        )