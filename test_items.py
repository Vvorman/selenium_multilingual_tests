from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30) # Раскомментируйте эту строку для визуальной проверки французской версии
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket button")
    assert button.is_displayed(), "Add to basket button is not displayed"