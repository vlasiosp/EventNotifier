from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


'''----------------------Time and Error Handling----------------------'''


def errhnd(browser):
    try:
        element = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.ID, 'facebook')))

    except TimeoutException:
        print("Time out!")

# Login function

def fb_login(browser, email, passw):
    browser.get('https://mobile.facebook.com')
    browser.find_element_by_id("m_login_email").send_keys(email)
    browser.find_element_by_id("m_login_password").send_keys(passw)
    browser.find_element_by_id('u_0_5').click()



# Facebook search function
def fb_search(browser, text):
    browser.find_element_by_id("search_jewel").click()
    search_box = browser.find_element_by_id('search-jewel-input-placeholder')
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, 'search-jewel-input-placeholder')))
    search_box.send_keys(text)
    search_box.send_keys(u'\ue007')


# Confirm saved login


def save_login(browser):
    btnsave = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "_54k8")))
    btnsave.click()
