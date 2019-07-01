
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.headless = False


# Create a new instance of the Chrome driver
browser = webdriver.Chrome(options=options, executable_path=r"E:\GitHub\EventNotifier\webdrivers\chromedriver.exe")
# go to the google home page
browser.get("http://www.google.com")

# find the element that's name attribute is q (the google search box)
inputElement = browser.find_element_by_name("q")

hobby = "εκδηλώσεις "
location = "χανια" \
           ""
# type in the search
inputElement.send_keys(hobby+location)
inputElement.send_keys(Keys.ENTER)

try:
    element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'Id_Of_Element')))
except TimeoutException:
    print("Time out!")



# the page is ajaxy so the title is originally this:
display.stop()

