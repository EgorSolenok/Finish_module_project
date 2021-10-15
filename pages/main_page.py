#!/usr/bin/env python3

import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By

# Инициализируем класс наследник MainPage для главной страницы сайта
class MainPage(BasePage):
    #определяем метод для открытия окна логина в систему
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        