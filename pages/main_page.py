#!/usr/bin/env python3

import pytest
import time
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    
def test_guest_can_go_to_login_page(browser): 
    browser.get(link) 
    go_to_login_page(browser) 