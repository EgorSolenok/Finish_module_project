#!/usr/bin/env python3

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import time
# Опредлеяем класс для базовой страницы веб-сайта
class BasePage():
    # Добавляем конструктор, передаем в него экземпляр драйвера и url адресс
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)   #команда для неявного ожидания, по умолчанию в 10 секунд
    # Добавляем метод открывающий страницу, использующий метод get()
    def open(self):
        self.browser.get(self.url)
        
    #реализация метода, в котором будем перехватывать исключение. how - как искать (css, id, xpath и тд) и собственно что "what" искать (строку-селектор). 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    #реализация метода, который  нужен для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert    # Переключаемся на алерт
        x = alert.text.split(" ")[2]    #парсим сообщения алерта, для получения значения x
        answer = str(math.log(abs((12 * math.sin(float(x))))))  #производим расчет
        alert.send_keys(answer) #Производим ввод ответа в окно alert
        alert.accept()
        try:
            alert = self.browser.switch_to.alert  # Переключаемся на алерт для считывания ответа системы на активацию кнопки на добавление в корзину
            alert_text = alert.text
            print(f"Your code: {alert_text}")   
            alert.accept()
            time.sleep
        except NoAlertPresentException:
            print("No second alert presented")