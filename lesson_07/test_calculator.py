import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)

    # 1. Открыть страницу калькулятора
    calculator.open()

    # 2. Ввести значение 45 в поле задержки
    calculator.set_delay(45)

    # 3. Нажать кнопки: 7, +, 8, =
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # 4. Проверить, что в окне отобразится результат 15 через 45 секунд (таймаут 50 сек)
    result = calculator.get_result(expected_text="15", timeout=50)
    assert result == "15", f"Ожидался результат '15', но на экране: '{result}'"
