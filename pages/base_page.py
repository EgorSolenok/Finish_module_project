#!/usr/bin/env python3

import pytest

# Опредлеяем класс для базовой страницы веб-сайта
class BasePage():
    # Добавляем конструктор, передаем в него экземпляр драйвера и url адресс
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    # Добавляем метод открывающий страницу, использующий метод get()
    def open(self):
        self.browser.get(self.url)