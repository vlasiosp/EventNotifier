from selenium import webdriver, functions
from selenium.webdriver.chrome.options import Options



'''----------------------Options----------------------'''


options = Options()


'''------------------Chrome options-----------'''


options.headless = False
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("detach", True)


# Pass the argument 1 to allow and 2 to block


options.add_experimental_option('prefs',{"profile.default_content_setting_values.notifications": 2})


'''------------------Firefox options-----------'''


# options.set_preference("dom.webnotifications.enabled", False)


'''----------------------Browser Definition----------------------'''


# Chrome


browser = webdriver.Chrome(options=options, executable_path=r'webdrivers/chromedriver.exe')


# Firefox


# browser = webdriver.Firefox(options=options, executable_path=r'webdrivers/geckodriver.exe')

'''----------------------Browsing----------------------'''

functions.fb_login(browser, 'teipir@gmail.com', '19eptalofou76')
functions.save_login(browser)
functions.fb_search(browser, 'Chania')



'''----------------------Closing Browser----------------------'''



#browser.close()
