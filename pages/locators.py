#!/usr/bin/env python3

import pytest
from selenium.webdriver.common.by import By

#определяем класс локаторов соответствующий MainPage. Для каждого класса PageObject - свой класс локаторов
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    PRICE_PRODUCT = (By.XPATH, "//*[@class='price_color'][1]")
    PRICE_BASKET_TOTAL = (By.XPATH, "//*[@id='messages']//p/strong")
    NAME_PRODUCT = (By.XPATH, "//li[@class='active']") 
    NAME_PRODUCT_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//div[@class='alertinner ']/strong[1]")  
    