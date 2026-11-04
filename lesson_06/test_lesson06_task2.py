from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    # Инициализируем явное ожидание (таймаут 10 секунд)
    wait = WebDriverWait(driver, 10)

    # 1. Открываем главную страницу для инициализации домена
    driver.get("https://gitflic.ru")
    
    # 2. Устанавливаем cookie пользователя 1
    user1_cookie = {
        'name': 'SESSION', 
        'value': 'ZWMzNmQ5MTYtZTQwNy00MjIzLTg3YzMtYjBhOWJhNDJlOWE0'
    }
    driver.add_cookie(user1_cookie)
    
    # 3. Обновляем страницу для применения cookie
    driver.refresh()
    
    # 4. Переходим на страницу профиля пользователя 1
    driver.get("https://gitflic.ru/user/test_lev_1") 

    # Ожидаем, пока URL не станет содержать юзернейм первого пользователя
    wait.until(EC.url_contains("test_lev_1"))
    
    # 5. Сохраняем текущий URL первого пользователя
    url_user_1 = driver.current_url
    
    # 6. Разлогиниваемся
    driver.delete_all_cookies()
    
    # 7. Устанавливаем cookie пользователя 2
    user2_cookie = {
        'name': 'SESSION', 
        'value': 'YWY4ZTljNDItMzZjMi00YjUwLWI2M2ItYWNjNWMyNjk2ZWM1'
    }
    driver.add_cookie(user2_cookie)
    
    # 8. Обновляем страницу
    driver.refresh()
    
    # 9. Переходим на страницу профиля пользователя 2
    driver.get("https://gitflic.ru/user/test_lev_2")

    # Ожидаем, пока URL не станет содержать юзернейм второго пользователя
    wait.until(EC.url_contains("test_lev_2"))
    
    # 10. Сохраняем текущий URL второго пользователя
    url_user_2 = driver.current_url
    
    # 11. Проверяем, что URL различаются
    assert url_user_1 != url_user_2

    driver.quit()
