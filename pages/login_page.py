#!/usr/bin/env python3

from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import faker
import time

class LoginPage(BasePage):
    # набор проверок для страницы логина - корректность ссылки, наличие формы регистрации и входа
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This page is not login page"
        
    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login  form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register  form is not presented"

    def register_new_user(self):
        # Метод для регистрации нового пользователя
        test_user = faker.Faker()       # Инициализация рандомизированных данных из библиотеки faker
        test_email = test_user.email()
        print("test email - ", test_email)
        test_password = "test_39_password"
        print("test_password - ", test_password)
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(test_email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(test_password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(test_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        
        
        
        
           