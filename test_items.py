#пригодится, когда будешь проверять
#import time
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_site_has_a_button_add_to_basket(browser):
    browser.get(LINK)
    #time.sleep(30)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) != 0, "Element not found"
