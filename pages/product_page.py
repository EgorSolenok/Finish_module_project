#!/usr/bin/env python3

import pytest
import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

# Инициализируем класс наследник BasePage для cтраницы сайта c продуктом
class ProductPage(BasePage):
    #определяем метод для добавления товара в корзину
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()   
    # Проверка присутствия кнопки добавления товара в корзину
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button with addition is not presented"
    
    #Проверка о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    def should_be_correct_name_product(self):
        time.sleep(2)
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text, "Name of added product is the same with actual name of product"#
        #print(self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text)
        #print(self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text)
        
        # Проверка на то, что цена товара соотвествует сумме в корзине
    def should_be_correct_price__product(self):
        time.sleep(2)
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL).text, "Price of added product is the same with actual sum in basket"#
        #print(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text)
        #print(self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL).text)
        