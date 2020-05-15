from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

id_email_locator = "email"
id_pass_locator = "pass"
email = "something@gmail.com"
pw = "password"
site_url = "https://www.facebook.com/"

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
try:
    chrome_driver.get(site_url)
    chrome_driver.find_element_by_id(id_email_locator).send_keys(email + Keys.TAB)
    chrome_driver.find_element_by_id(id_pass_locator).send_keys(pw + Keys.ENTER)

except type:
    print("test failed")
finally:
    time.sleep(3)
    chrome_driver.close()










