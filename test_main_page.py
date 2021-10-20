#!/usr/bin/env python3

import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium import webdriver
import time

# Тестовый класс для главной страницы со стороны гостя.
@pytest.mark.login_guest
class TestLoginFromMainPage(): 
    
    # Тест, проверяющий возможность перехода на страницу логина
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        # Инициализируем Page Object, передаем в конструктор экземпляр
        # драйвера и url адрес 
        page.open()      #открываем страницу
        page.go_to_login_page()
        # Выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) 
        # Явно инициализируем страницу логина в браузер
        login_page.should_be_login_page() 
        # Осуществляем проверку страницы с логином
        
    # Тест, проверяющий наличия ссылки на переход на логин
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
         # Проверяем наличие ссылки на страницу логина
        page.should_be_login_link()
        
# Тест, проверяющий отсутсвие добавленных товаров в корзине, 
# наличия сообщения о пустой корзине.
# 1) Гость открывает главную страницу 
# 2) Переходит в корзину по кнопке в шапке сайта
# 3) Ожидаем, что в корзине нет товаров
# 4) Ожидаем, что есть текст о том что корзина пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()    #метод перехода на строницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_message_of_empty_basket()
    