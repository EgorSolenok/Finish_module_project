#!/usr/bin/env python3

import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium import webdriver
import time

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()      #открываем страницу
#    page.go_to_login_page()
#    #выполняем метод страницы - переходим на страницу логина
#    login_page = LoginPage(browser, browser.current_url) 
#    #явно инициализируем страницу логина в браузер
#    login_page.should_be_login_page() 
#    #осуществляем проверку страницы с логином
#    
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()    #метод проверки 

"""Гость открывает главную страницу 
Переходит в корзину по кнопке в шапке сайта
Ожидаем, что в корзине нет товаров
Ожидаем, что есть текст о том что корзина пуста"""
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()    #метод перехода на строницу корзины
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_message_of_empty_basket()
    