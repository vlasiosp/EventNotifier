from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import random


options = Options()
options.headless = False
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2  # block notifications
})


browser = webdriver.Chrome(options=options, executable_path=r'webdrivers/chromedriver.exe')


# Login function
def fb_login(email, passw):
    browser.get('https://www.facebook.com')
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pass").send_keys(passw)
    browser.find_element_by_id('loginbutton').click()


# Search function
def fb_search(text):
    browser.find_element_by_class_name('_1frb').send_keys(text)
    browser.find_element_by_css_selector("button[data-testid='facebar_search_button']").click()


fb_login('teipir@gmail.com', '19eptalofou76')
fb_search('Champions')


try:
    element = WebDriverWait(browser, random.randrange(1,4,1)).until(EC.presence_of_element_located((By.ID, 'facebook')))
    display.stop()
except TimeoutException:
    print("Time out!")


browser.close()
