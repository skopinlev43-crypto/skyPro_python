from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    # Инициализируем браузер Safari
    safari_driver = webdriver.Safari()
    safari_driver.maximize_window()
    safari_driver.implicitly_wait(10)
    yield safari_driver
    safari_driver.quit()

def test_form_validation(driver):
    # 1. Открываем оригинальную страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # 2. Заполняем форму значениями
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear() 
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    # 3. Находим кнопку Submit и скроллим к ней нативными средствами Selenium
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    ActionChains(driver).scroll_to_element(submit_button).perform()
    
    submit_button.click()
    
    # 4. Ожидание обновления DOM-страницы
    wait = WebDriverWait(driver, 10)
    
    # Ждем, пока старая кнопка Submit исчезнет из DOM, сигнализируя о том, что Safari обновил окно
    wait.until(EC.staleness_of(submit_button))
    
    # Дожидаемся появления элемента Zip code в DOM-дереве новой страницы и проверяем его класс
    zip_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_field.get_attribute("class"), "Поле Zip code должно быть подсвечено красным!"
    
    # 5. Проверяем остальные поля на наличие класса "alert-success"
    green_fields_ids = [
        "first-name", "last-name", "address", "e-mail", 
        "phone", "city", "country", "job-position", "company"
    ]
    
    for field_id in green_fields_ids:
        field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым!"
