#!/usr/bin/env python3

from selenium.webdriver.common.by import By


# Определяем класс локаторов соответствующий BasePage.
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(@href, 'basket')][@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# Определяем класс локаторов соответствующий BasketPage.
class BasketPageLocators:
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
    MESSAGE_OF_EMPTY_BASKET = (By.XPATH, "//*[@id='content_inner']/p")


# Определяем класс локаторов соответствующий LoginPage.
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.XPATH, "//*[@id='id_registration-email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='id_registration-password1']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//*[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']/button")


# Определяем класс локаторов соответствующий MainPage. Для каждого класса PageObject - свой класс локаторов
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# Определяем класс локаторов соответствующий ProductPage.  
class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    PRICE_PRODUCT = (By.XPATH, "//*[@class='price_color'][1]")
    PRICE_BASKET_TOTAL = (By.XPATH, "//*[@id='messages']//p/strong")
    NAME_PRODUCT = (By.XPATH, "//li[@class='active']")
    NAME_PRODUCT_IN_MESSAGE = (By.XPATH, "//*[@id='messages']//div[@class='alertinner ']/strong[1]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div")
