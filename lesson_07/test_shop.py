import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    # Гарантированное закрытие, если браузер еще открыт
    if browser.service.process:
        browser.quit()


def test_saucedemo_checkout(driver):
    # Инициализация объектов страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт магазина
    login_page.open()

    # 2. Авторизоваться как пользователь standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить в корзину товары
    inventory_page.add_backpack()
    inventory_page.add_bolt_tshirt()
    inventory_page.add_onesie()

    # 4. Перейти в корзину
    inventory_page.go_to_cart()

    # Дополнительная проверка содержимого корзины через метод CartPage
    items_in_cart = cart_page.get_cart_items_names()
    expected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    assert items_in_cart == expected_items, f"Ожидались товары {expected_items}, но в корзине {items_in_cart}"

    # 5. Нажать кнопку Checkout
    cart_page.click_checkout()

    # 6. Заполнить форму своими данными и нажать Continue
    checkout_page.fill_customer_info("Иван", "Иванов", "123456")
    checkout_page.click_continue()

    # 7. Прочитать со страницы итоговую стоимость (Total)
    total_text = checkout_page.get_total_text()

    # 8. Закрыть браузер (согласно строгому порядку шагов в задании)
    driver.quit()

    # 9. Проверить (assert), что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_text, f"Ожидалось $58.29, но получили: {total_text}"
