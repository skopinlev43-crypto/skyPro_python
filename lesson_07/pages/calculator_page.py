from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    
    # Локаторы элементов страницы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        """Очищает поле задержки и вводит указанное количество секунд."""
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        """Нажимает на любую кнопку калькулятора по её тексту (цифры, операторы, '=')."""
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self, expected_text, timeout=50):
        """Ожидает появления ожидаемого текста на экране и возвращает текущее значение."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.SCREEN, str(expected_text)))
        return self.driver.find_element(*self.SCREEN).text
