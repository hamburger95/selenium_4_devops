from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "somthing@gmail.com"
pw = "!@$@$$@"
site_url = "https://github.com/"

chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
try:
    chrome_driver.get(site_url)

    chrome_driver.implicitly_wait(10)
    chrome_driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label").send_keys("selenium" + Keys.ENTER)

except type:
    print("test failed")
finally:
    time.sleep(10)
    chrome_driver.close()
