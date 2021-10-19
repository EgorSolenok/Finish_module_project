#!/usr/bin/env python3

import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


# Инициализируем класс наследник MainPage для главной страницы сайта
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
            