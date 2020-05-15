from selenium import webdriver
from selenium.webdriver.common.keys import Keys

expected = "5.00"
my_driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")

my_driver.get("C:/Users/user/Desktop/tip_calc/index.html")

# my_driver.get("https://www.google.com")
# my_driver.find_element_by_name("q").send_keys("Ido Hamburger")
# my_driver.find_element_by_id("gsr").click()

# //*[@id="serviceQual"]

# /html/body/div/div[1]/form/p[4]/select

my_driver.find_element_by_xpath('//*[@id="billamt"]').send_keys(100)

my_driver.find_element_by_xpath('//*[@id="serviceQual"]').send_keys(20)u

my_driver.find_element_by_xpath('//*[@id="peopleamt"]').send_keys("5" + Keys.TAB)

my_driver.find_element_by_xpath('//*[@id="musicamt"]').send_keys(5)

my_driver.find_element_by_xpath('//*[@id="calculate"]').click()

result = my_driver.find_element_by_id("tip").text

assert result == expected  # check if true








