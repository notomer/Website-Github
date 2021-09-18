#  Libraries
from selenium import webdriver
import urllib.request
import urllib.parse
import re

# Login Info
username = "1024068"
password = "only1Allah"
code = "LCPS"
# URL
url = "https://launchpad.classlink.com/login"
# Chrome Driver


class edmuntum():

    driver = webdriver.Chrome("/Users/omerkhan/downloads/chromedriver")

    driver.get(url)
    # Classlink Login
    formfill = driver.find_element_by_id
    formfill("username").send_keys(username)
    formfill("password").send_keys(password)
    formfill("code").send_keys(code)
    formfill("signin").click()

    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]").click()

    driver.get("https://launchpad.classlink.com/browsersso/445673")

    installextensionpass = "btn btn-default js-btn-continue-to-site"

    classclick = driver.find_element_by_class_name

    classclick(installextensionpass)

    mcrsftloguser = "1024068@lcps.org"
    mcrsftlogpass = "only1Allah"


    formfill("idSIButton9").click()

    formfill("i0118").send_keys(mcrsftlogpass)

    formfill("mcrsftsub").click()

    formfill("KmsiCheckboxField").click()

    formfill("idSIButton9").click()
