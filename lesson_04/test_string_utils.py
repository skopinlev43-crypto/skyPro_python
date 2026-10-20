import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()

# ==========================================
# ТЕСТЫ ДЛЯ МЕТОДА capitalize
# ==========================================

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),         # На входе нижний регистр
    ("Skypro", "Skypro"),         # На входе уже с заглавной буквы
    ("SKYPRO", "Skypro"),         # На входе верхний регистр (ОШИБКА: метод ломает остальные буквы)
    ("123sky", "123sky"),         # Строка начинается с цифры
    ("", ""),                     # Пустая строка
    ("   sky", "   sky"),         # Строка начинается с пробела
    ("s", "S"),                   # Строка из одного символа
])
def test_capitalize_positive_and_boundary(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


# ==========================================
# ТЕСТЫ ДЛЯ МЕТОДА trim
# ==========================================

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),      # Несколько пробелов в начале
    (" skypro", "skypro"),        # Один пробел в начале
    ("skypro   ", "skypro   "),    # Пробелы только в конце (не должны удаляться)
    ("  sky  pro  ", "sky  pro  "), # Пробелы в начале, середине и конце
    ("skypro", "skypro"),         # Без пробелов
    ("   ", ""),                  # Строка только из пробелов
    ("", ""),                     # Пустая строка
])
def test_trim_positive_and_boundary(utils, input_str, expected):
    assert utils.trim(input_str) == expected


# ==========================================
# ТЕСТЫ ДЛЯ МЕТОДА contains
# ==========================================

@pytest.mark.parametrize("input_str, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "S", True),         # Символ в начале
    ("SkyPro", "y", True),         # Символ в середине
    ("SkyPro", "o", True),         # Символ в конце
    ("SkyPro", "Pro", True),       # Поиск целой подстроки
    # Негативные сценарии
    ("SkyPro", "U", False),        # Символа нет в строке
    ("SkyPro", "s", False),        # Поиск с учетом регистра (символ в другом регистре)
    ("", "A", False),              # Поиск в пустой строке
])
def test_contains_positive_and_negative(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "", True),          # Передан пустой символ (ОШИБКА: index() падает на пустой строке, возвращает False вместо True/ошибки)
])
def test_contains_boundary_empty_symbol(utils, input_str, symbol, expected):
    # Тест упадет, так как метод содержит ошибку логики при обработке пустой строки
    assert utils.contains(input_str, symbol) == expected


# ==========================================
# ТЕСТЫ ДЛЯ МЕТОДА delete_symbol
# ==========================================

@pytest.mark.parametrize("input_str, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "k", "SyPro"),      # Удаление одного символа
    ("SkyPro", "Pro", "Sky"),      # Удаление подстроки
    ("Ananas", "a", "Anns"),       # Удаление символа, который повторяется (регистрозависимо)
    # Негативные сценарии / Граничные условия
    ("SkyPro", "U", "SkyPro"),     # Символа для удаления нет в строке
    ("SkyPro", "", "SkyPro"),      # Передан пустой символ для удаления (ОШИБКА: из-за бага в contains вернет пустую строку)
    ("", "k", ""),                 # Удаление из пустой строки
])
def test_delete_symbol(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
