import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    # Инициализация браузера Firefox
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    # 11. Закройте браузер.
    driver.quit()


def test_saucedemo_checkout(driver):
    # 1. Откройте сайт магазина в FireFox.
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуйтесь как пользователь standard_user.
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавьте в корзину товары: Sauce Labs Backpack, Bolt T-Shirt, Onesie.
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # 4. Перейдите в корзину.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 5. Нажмите Checkout.
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс.
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Иванов")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитайте со страницы итоговую стоимость ( Total ).
    total_element_text = driver.find_element(
        By.CLASS_NAME, "summary_total_label"
    ).text

    # 9. Проверьте, что итоговая сумма равна $58.29.
    # Строка содержит текст "Total: $58.29", поэтому проверяем вхождение или точное совпадение
    assert (
        "Total: $58.29" in total_element_text
    ), f"Ожидалось $58.29, но получили: {total_element_text}"
