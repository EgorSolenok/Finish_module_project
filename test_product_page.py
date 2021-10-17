#!/usr/bin/env python3

import pytest
from .pages.product_page import ProductPage
from selenium import webdriver
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                 ]
                        )
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
    