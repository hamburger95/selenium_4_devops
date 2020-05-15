from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

xpath_locator = '//*[@id="source"]'
class_locator = "orig.tlid-source-text-input.goog-textarea"
id_locator = "source"

site_url = "https://translate.google.com/"
text = "Hi there, this is DevOps Expert student.."

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
chrome_driver.get(site_url)

try:
    id_elem = chrome_driver.find_element_by_id(id_locator).send_keys(text + Keys.ENTER)
    class_elem = chrome_driver.find_element_by_class_name(class_locator).send_keys(text + Keys.ENTER)
    xpath_elem = chrome_driver.find_element_by_xpath(xpath_locator).send_keys(text + Keys.ENTER)
except type:
    print("test failed")
finally:
    time.sleep(5)
    chrome_driver.close()










