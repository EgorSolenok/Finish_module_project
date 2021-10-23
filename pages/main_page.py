#!/usr/bin/env python3

from .base_page import BasePage


# Инициализируем класс наследник MainPage для главной страницы сайта.
# Класс принимает аргументы и передает в конструктор класса предка.
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        