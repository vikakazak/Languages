import time

def test_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_add_to_basket = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button_add_to_basket, "Add to basket button is not displayed"