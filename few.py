from selenium import webdriver

locator = "cell.cwide.layout1"
firefox_driver = webdriver.Firefox(executable_path="C:/geckodriver.exe")
chrome_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
site_url = "https://www.ynet.co.il/home/0,7340,L-8,00.html"

firefox_driver.get(site_url)
chrome_driver.get(site_url)

firefox_elem = firefox_driver.find_element_by_class_name(locator).text
chrome_elem = chrome_driver.find_element_by_class_name(locator).text

firefox_driver.close()
chrome_driver.close()

assert firefox_elem == chrome_elem





