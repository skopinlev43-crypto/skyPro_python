import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Инициализация драйвера Google Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Закрытие браузера после завершения теста
    driver.quit()

def test_slow_calculator(driver):
    # 1. Откройте страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html ")

    # 2. В поле ввода по локатору #delay введите значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажмите на кнопки: 7, +, 8, =
    # Поиск кнопок на основе их текстового содержимого внутри тегов span
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
    # Задаем таймаут с небольшим запасом (50 секунд)
    wait = WebDriverWait(driver, 50)
    
    screen = driver.find_element(By.CLASS_NAME, "screen")
    
    # Ожидаем, пока в элементе экрана калькулятора появится текст "15"
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    # Финальная проверка (assert)
    assert screen.text == "15", f"Ожидался результат '15', но на экране: '{screen.text}'"
