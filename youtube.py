
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

site_url = "https://www.youtube.com/"

song = "בין קודש לחול"

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
chrome_driver.get(site_url)

try:

    chrome_driver.find_element_by_id("search-form").click()
    chrome_driver.find_element_by_name("search_query").send_keys(song + Keys.ENTER)

except type:
    print("test failed")
finally:
    time.sleep(5)
    # chrome_driver.close()
