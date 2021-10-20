#!/usr/bin/env python3

import pytest
import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

# Инициализируем класс наследник BasePage для cтраницы сайта c продуктом
class ProductPage(BasePage):
    
    # Определяем метод для добавления товара в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.
                                         BUTTON_ADD_TO_BASKET)
        link.click()   
    
    # Проверка присутствия кнопки добавления товара в корзину
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.
                                       BUTTON_ADD_TO_BASKET), \
        "Button with addition is not presented"
    
    # Проверка о том, что товар добавлен в корзину. Название товара в сообщении
    # должно совпадать с тем товаром, который вы действительно добавили.
    def should_be_correct_name_product(self):
        assert self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT).text == \
        self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).\
        text, "Name of added product is the same with actual name of product"
        
    # Проверка на то, что цена товара соотвествует сумме в корзине
    def should_be_correct_price__product(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT).text == \
        self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL)\
        .text, "Price of added product is the same with actual sum in basket"#
        
    # Проверка на отсутсвие сообщения об умпешном добавлении в корзину.
    # Проверка упадет, как только увидит искомый элемент. Не появился: успех,
    # тест зеленый.
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.
                                           SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
        
    # Метод, проверяющий что элемент пропадет в течении установленного времени
    # либо его изначальное отсутствие.Проверка будет ждать до тех пор, пока 
    # элемент не исчезнет. Сообщение появилось и исчезло - тест прошел,
    # сообщение не пропало - тест упал. Сообщение не появилось - все ок.
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is not dissapear, but should be"