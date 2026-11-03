from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 1. Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 2. Проверяем, что количество ссылок равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # 3. Проверяем в цикле, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed(), f"Ссылка с текстом '{link.text}' не отображается"

    # 4. Проверяем, что текст первой ссылки содержит "1"
    assert "1" in links[0].text, f"Текст первой ссылки ('{links[0].text}') не содержит '1'"

    driver.quit()
