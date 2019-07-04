# Login function
def fb_login(email, passw):
    browser.get('https://www.facebook.com')
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pass").send_keys(passw)
    browser.find_element_by_id('loginbutton').click()


# Facebook earch function
def fb_search(text):
    browser.find_element_by_class_name('_1frb').send_keys(text)
    browser.find_element_by_css_selector("button[data-testid='facebar_search_button']").click()