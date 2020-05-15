from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


site_url = "https://www.google.co.il/"

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
try:
    chrome_driver.get(site_url)
    print("before cleaning: ", chrome_driver.get_cookies())
    chrome_driver.delete_all_cookies()
    print("after cleaning: ", chrome_driver.get_cookies())
except type:
    print("test failed")
finally:
    time.sleep(3)
    chrome_driver.close()
