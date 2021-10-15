#!/usr/bin/env python3

import pytest
from selenium.webdriver.common.by import By

#определяем класс локаторов соответствующий MainPage. Для каждого класса PageObject - свой класс локаторов
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")