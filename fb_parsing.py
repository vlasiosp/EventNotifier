from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = False
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2  #block notifications
})

browser = webdriver.Chrome(options=options, executable_path=r"E:\GitHub\EventNotifier\webdrivers\chromedriver.exe")
# go to the google home page



def fb_login(email, passw):

    browser.get('https://www.facebook.com')
    browser.find_element_by_id("email").send_keys(email)
    browser.find_element_by_id("pass").send_keys(passw)
    browser.find_element_by_id('loginbutton').click()




fb_login("teipir@gmail.com","19eptalofou76")



try:
    element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'Id_Of_Element')))
except TimeoutException:
    print("Time out!")



# the page is ajaxy so the title is originally this:
display.stop()
