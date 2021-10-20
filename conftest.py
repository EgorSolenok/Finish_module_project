#!/usr/bin/env python3

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавление возможности параметризации окружения, используя различные языки
# интерфейса. Для изменения языка необходимо в командной строке явно указать:
# <--language=ru> или другой язык в стандартном сокращении. 
def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store', 
                     default='en',
                     help="Choose language: ru, en, fr, it, es ... (etc._)"
                    )


# Инициализация метода для использования драйвера браузера Chrome, обернутого
# в фикстуру для использования в каждом тесте. Возвращает экземпляр браузера.
# Явно закрывает браузер после каждого теста.
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    # Опция для запуска тестов в развернутом окне браузера
    options.add_argument("start-maximized")
    # Опция для запуска тестов с различным языком интерфейса
    options.add_experimental_option(
        'prefs',{'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    
    browser = webdriver.Chrome(options=options)
    
    yield browser   # Возвращает объект драйвера Chrome
    print("\nquit browser..")
    browser.quit()