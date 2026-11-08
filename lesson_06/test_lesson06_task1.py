from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    # 1. Открываем страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Находим и нажмимаем на кнопку "Start"
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дожидаемся появления текста "Hello World!"
    finish_text_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Делаем скриншот страницы
    driver.save_screenshot("page_screenshot.png")

    # 5. Проверяем, что появившийся текст равен "Hello World!"
    assert finish_text_element.text == "Hello World!"

    driver.quit()
