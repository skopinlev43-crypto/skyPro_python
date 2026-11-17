from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bolt_tshirt_add_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.driver.find_element(*self.backpack_add_btn).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(*self.bolt_tshirt_add_btn).click()

    def add_onesie(self):
        self.driver.find_element(*self.onesie_add_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
