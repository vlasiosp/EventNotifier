from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Login function
def fb_login(browser, email, passw):
    browser.get('https://mobile.facebook.com')
    browser.find_element_by_id("m_login_email").send_keys(email)
    browser.find_element_by_id("m_login_password").send_keys(passw)
    browser.find_element_by_id('u_0_5').click()


# Facebook earch function
def fb_search(browser, text):
    browser.find_element_by_id("search_jewel").click()
    browser.find_element_by_class_name('_19no').send_keys(text)
    browser.find_element_by_css_selector("button[data-testid='facebar_search_button']").click()

# Confirm saved login

def save_login(browser):
    btnsave = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "_54k8")))
    btnsave.click()

#def save_login(browser):
    #chksave = browser.find_element_by_xpath("/*[html@data-autoid = 'autoid_1']")
