import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываем исходную страницу
    driver.get("https://httpbin.qa-territory.online/")
    
    time.sleep(1)

    # 2. Находим и кликаем на ссылку "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()
    
    time.sleep(1)

    # 3. Проверяем, что URL изменился на /forms/post
    expected_form_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url == expected_form_url

    # 4. Возвращаемся назад на главную страницу
    driver.back()
    
    time.sleep(1)

    # 5. Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online/"


    driver.quit()
