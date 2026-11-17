from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_items_names(self):
        elements = self.driver.find_elements(*self.cart_items)
        return [element.text for element in elements]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
