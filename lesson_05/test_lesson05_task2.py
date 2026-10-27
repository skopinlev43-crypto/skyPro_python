from selenium import webdriver
from selenium.webdriver.common.by import By
import time

    
def test_form_submission():
    driver = webdriver.Chrome()
    # 1. Открываем исходную страницу
    driver.get("https://httpbin.qa-territory.online/forms/post")
    
    time.sleep(1)

    # 2. Находим поле "custname" и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Лев")

    # 3. Находим кнопку "submit" и жмем на нее
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_button.click()

    time.sleep(2)

    # 4. Проверяем изменение URL
    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
