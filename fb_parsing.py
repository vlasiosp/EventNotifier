import functions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


functions.fb_login(browser, 'teipir@gmail.com', '19eptalofou76')
functions.fb_search(browser, 'Champions')


try:
    element = WebDriverWait(browser, random.randrange(1,4,1)).until(EC.presence_of_element_located((By.ID, 'facebook')))

except TimeoutException:
    print("Time out!")

display.stop()
browser.close()
