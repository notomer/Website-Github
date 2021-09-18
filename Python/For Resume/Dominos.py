#  Libraries 
from selenium import webdriver
import urllib.request
import urllib.parse
import re

# Login Info 
user = "lolaughtority@gmail.com"
password = "only1Allah"
# URL
url = "https://www.dominos.com/en/"
# Chrome Driver
driver = webdriver.Chrome("/Users/omerkhan/downloads/chromedriver")

driver.get(url)
# dominos Login

id = driver.find_element_by_id
xpath = driver.find_element_by_xpath

xpath("//*[@id=_dpz]/header/nav[1]/div[1]/div[3]/a")

id("_dpz").click()


id("username").send_keys(user)
id("password").send_keys(password)
id("signin").click()





