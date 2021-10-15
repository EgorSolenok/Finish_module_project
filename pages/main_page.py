#!/usr/bin/env python3

import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

# Инициализируем класс наследник MainPage для главной страницы сайта
class MainPage(BasePage):
    #определяем метод для открытия окна логина в систему
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()   
        
    #Определяем метод проверки ссылки на логин
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login  link is not presented"
        