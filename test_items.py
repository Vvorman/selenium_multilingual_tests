import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element('xpath', "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button.is_displayed(), "Add to basket button is not displayed"
