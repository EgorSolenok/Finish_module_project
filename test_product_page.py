#!/usr/bin/env python3

import pytest
from .pages.product_page import ProductPage
from selenium import webdriver
import time


#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#                                 ]
#                        )
#def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()      #открываем страницу
#    page.should_be_button_add_to_basket()
#    page.add_to_basket()
#    #выполняем метод страницы - кликаем на кнопку добавления в корзину товара
#    page.solve_quiz_and_get_code()
#    page.should_be_correct_name_product()
#    page.should_be_correct_price__product()    

#@pytest.mark.xfail
#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()      #открываем страницу
#    page.should_be_button_add_to_basket()
#    page.add_to_basket()
#    page.should_not_be_success_message()
    
#def test_guest_cant_see_success_message(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()      #открываем страницу
#    page.should_not_be_success_message()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.xfail
#def test_guest_shoud_see_message_disappeared_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()      #открываем страницу
#    page.add_to_basket()
#    page.should_disappear_success_message()