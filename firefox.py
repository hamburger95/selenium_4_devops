from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep

try:

    # setting webdriver
    driver = webdriver.Firefox(executable_path="C:/geckodriver.exe")
    driver.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")

    # get page title
    title = driver.title
    print(title)

    # get site name
    site_name = driver.current_url
    print(site_name)

    # compare results
    assert title != site_name

except type:
    print("Something went wrong...")





