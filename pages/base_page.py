#!/usr/bin/env python3

import pytest
from selenium.common.exceptions import NoSuchElementException
# Опредлеяем класс для базовой страницы веб-сайта
class BasePage():
    # Добавляем конструктор, передаем в него экземпляр драйвера и url адресс
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   #команда для неявного ожидания, по умолчанию в 10 секунд
    # Добавляем метод открывающий страницу, использующий метод get()
    def open(self):
        self.browser.get(self.url)
        
    #реализация метода, в котором будем перехватывать исключение. how - как искать (css, id, xpath и тд) и собственно что "what" искать (строку-селектор). 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    