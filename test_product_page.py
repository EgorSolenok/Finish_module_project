#!/usr/bin/env python3

import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium import webdriver
import time

# Инициализация тестового класса для пользователя. Реализована 
# регистрация в каждом тесте с использованием рандомных данных, 
# предоставляемых библиотекой Faker. Удаление пользователей не реализовано.
class TestUserAddToBasketFromProductPage():
    # Метод, исполянющийся каждую функцию в классе для регистрации
    # пользователя. Также проверяет удачную авторизацию по наличию иконки 
    # логина. Исполняется до начала каждого теста. 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user()
        new_page = MainPage(browser, browser.current_url)
        new_page.should_be_authorized_user()

    # Тест ождидающий, что пользователю не отображется сообщение о 
    # добавленном товаре, так как его не добавляли.
    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        # инициализируем Page Object, передаем в конструктор экземпляр 
        # драйвера и url адрес 
        page.open()      # Открываем страницу
        page.should_not_be_success_message() # Проверяем отсутсвие сообщения
        
    # Тест, ожидающий что пользователь после добавления товара в корзину
    # видит корректное название товара в сообщении об успешном добавлении.
    # Сравнивает цену товара и суммарную стоимость корзины. Реализован в
    # промоакции, и следовательно использует метод для решения задачи
    # для возможности успешного добавления.
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        # инициализируем Page Object, передаем в конструктор экземпляр
        # драйвера и url адрес 
        page.open()      #открываем страницу
        page.should_be_button_add_to_basket()
        #выполняем метод страницы - кликаем на кнопку добавления в
        # корзину товара
        page.add_to_basket()
        # Решаем задачу и вводим ответ
        page.solve_quiz_and_get_code()
        # Сравнение имени
        page.should_be_correct_name_product()
        # Сравнение цены
        page.should_be_correct_price__product() 

# Тест, ожидающий что гость после добавления товара в корзину
# видит корректное название товара в сообщении об успешном добавлении.
# Сравнивает цену товара и суммарную стоимость корзины. Реализован в
# промоакции, и следовательно использует метод для решения задачи
# для возможности успешного добавления. Добавлена параметризация для 
# нескольких ссылок. 
@pytest.mark.parametrize('link', [
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
 pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      #открываем страницу
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    #выполняем метод страницы - кликаем на кнопку добавления в корзину товара
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_product()
    page.should_be_correct_price__product() 
    
# Тест, ождиающий что гость не добавив товара в корзину, не будет
# видеть на странице корзины товары или сообщения об добавлении.
# 1) Гость открывает страницу товара
# 2) Переходит в корзину по кнопке в шапке 
# 3) Ожидаем, что в корзине нет товаров
# 4) Ожидаем, что есть текст о том что корзина пуста """
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      #открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_message_of_empty_basket()

# Тест, ожидающий что после добавления товара в корзину гость не увидит
# сообщения об успешном добавлении. Помечен как заведомо падающий, так как
# в позитивном сценарии нормальной работы веб-сервиса - сообщение появиться.
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      #открываем страницу
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    page.should_not_be_success_message()

# Тест, ожидающий что гость не видит сообщения об успешном добавлении
# продукта. Проходит, так как сообщения и не будет, не добавив товар.
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      #открываем страницу
    page.should_not_be_success_message()

# Тест для определения возможности перехода на страницу логина для гостя.
# Проверяет работоспособность ссылки.
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# Тест, проверяющий наличие ссылки на переход на страницу логина со страницы
# продукта.
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Тест, который ожидает, что гость не увидит сообщения о добавлении товара.
# Помечен как заведомо падающий, так как при нормальной работе веб-сервиса 
# сообщение будет отображено.
@pytest.mark.xfail
def test_guest_shoud_see_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()      #открываем страницу
    page.add_to_basket()
    page.should_disappear_success_message()