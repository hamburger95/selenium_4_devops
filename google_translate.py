from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

xpath_locator = "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"
class_locator = "tlid-translation translation"
site_url = "https://translate.google.com/"
hebrew_text = "מה המצב רעות? איך הולך עם ההרדמות???"

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
chrome_driver.get(site_url)

try:
    chrome_driver.find_element_by_xpath(xpath_locator).click()
    chrome_driver.find_element_by_id("sl_list-search-box").send_keys("Hebrew" + Keys.ENTER)
    chrome_driver.find_element_by_id("source").send_keys(hebrew_text + Keys.ENTER)
    chrome_driver.implicitly_wait(10)
    get_translation_by_class_name = chrome_driver.find_element_by_class_name("result-shield-container.tlid-copy-target").text
    get_translation_by_xpath = chrome_driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div").text
    assert get_translation_by_xpath == get_translation_by_class_name
    print(get_translation_by_class_name)
    print(get_translation_by_xpath)
except type:
    print("test failed")
finally:
    time.sleep(3)
    # chrome_driver.close()









