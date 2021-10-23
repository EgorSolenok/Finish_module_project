#!/usr/bin/env python3

import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


# Опредлеяем класс для базовой страницы веб-сайта
class BasePage:
    # Добавляем конструктор, передаем в него экземпляр драйвера и url адресс
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        # Команда для неявного ожидания каждой инструкции find_element,
        # по умолчанию в 5 секунд
        self.browser.implicitly_wait(timeout)

        # Добавляем метод открывающий страницу, использующий метод get()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Метод, реализующий переход на страницу корзины. Не используется на
    # самой странице корзины!!!
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    # Метод, позволяющий определить, что элемента нет на странице и не
    # появляется в течение 4х секунд. Передаем в метод способ локатора
    # и его локатор.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Метод, в котором будем перехватывать исключение. how - как искать 
    # (css, id, xpath и тд) и собственно что "what" искать (строку-селектор). 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Метод, в котором будем перехватывать исключение. how - как искать (
    # css, id, xpath и тд) и собственно что "what" искать (строку-селектор). 
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # Метод, который открывает переданный в качестве аргумента адрес.
    def open(self):
        self.browser.get(self.url)

        # Проверка на то, что пользователь залогинен (по иконке пользователя)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented,probably unauthorised user"

    # Проверка на наличие ссылки на переход на страницу логина  
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    # Метод, который  нужен для проверки того, что вы написали тест на Selenium.
    # После этого вы получите код, который нужно ввести в качестве ответа на данное
    # задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете
    # тест. Не забудьте в конце теста добавить проверки на ожидаемый результат
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert  # Переключаемся на алерт
        # парсим сообщения алерта, для получения значения x
        x = alert.text.split(" ")[2]
        # производим расчет
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)  # Производим ввод ответа в окно alert
        alert.accept()
        try:
            # Переключаемся на алерт для считывания ответа системы на 
            # активацию кнопки на добавление в корзину
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
