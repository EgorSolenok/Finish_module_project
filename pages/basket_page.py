#!/usr/bin/env python3

import pytest
import time
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

# Инициализируем класс наследник BasePage для cтраницы сайта c продуктом
class BasketPage(BasePage):
    
    #Метод, ожидающий того, что корзина пустая - элементов на покупок нету.
    # Если есть - падает с ошибкой. 
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
        "Basket items is presented, but should not be"
        
    #Метод, проверяющий сообщение о пустой корзине. Реализован для русского
    # и английского языка интерфейса
    def should_be_message_of_empty_basket(self):
        language = self.browser.execute_script("return window.navigator.\
        userLanguage || window.navigator.language")
        if language == "en":
            assert "Your basket is empty" in self.browser.find_element(
                *BasketPageLocators.MESSAGE_OF_EMPTY_BASKET).text.strip(),\
            "Invalid message of empty basket"
        if language == "ru":
            assert "Ваша корзина пуста" in self.browser.find_element(
                *BasketPageLocators.MESSAGE_OF_EMPTY_BASKET).text.strip(),\
            "Invalid message of empty basket"