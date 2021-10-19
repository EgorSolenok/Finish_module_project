#!/usr/bin/env python3

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store', 
                     default='en',
                     help="Choose language: ru, en, fr, it, es ... (etc._)"
                    )

    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("detach", True)   # Опция, которая выключает автозакрытие браузера после теста
    options.add_argument("start-maximized")
#    options.add_argument("--auto-open-devtools-for-tabs") # Опция для авто включения devtools 
    options.add_experimental_option(
        'prefs',{'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()