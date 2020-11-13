# -*- coding: utf-8 -*-
import selenium.webdriver 
from selenium import webdriver
from time import sleep
import requests
import json
import pandas as pd 
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
from python_anticaptcha import AnticatpchaException, ImageToTextTask
import time,os,datetime
from selenium import webdriver
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv
from faker import Faker 
fake = Faker()
import random
requests.packages.urllib3.disable_warnings()
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Function that loads the site
def loadsite() :
    global driver,RFC,PASSWORD,ij,NO_OF_ACCOUNT_TO_BE_CREATED
    
    print("Loading site started..........")
    #driver.maximize_window()
    print('Logging out...')
    print('\nRegistering New User no '+str(ij))
    driver.get('https://do512.com/users/sign_out')
    sleep(4)
    driver.get("https://do512.com/users/sign_up")
    print("Wbsite link called")
    print("Waiting for output from website...")
    
    sleep(5)

    # Check if the webpage is correctly loaded
    try:
        
        #capcha_answer = str(captcha_solver())
        user_row = []
        x = fake.profile()
        year = x['birthdate'].strftime("%Y")
        month = x['birthdate'].strftime("%m")
        day = x['birthdate'].strftime("%d")
        mail = x['mail']
        fname = x['name'].split()[0]
        lname = x['name'].split()[1]
        password = ''.join(random.choice('012345678abcdefghij') for i in range(8))

        print('email = '+str(mail))

        user_row.append(mail)
        user_row.append(password)
        user_row.append(fname)
        user_row.append(lname)
        user_row.append(day)
        user_row.append(month)
        user_row.append(year)
        user_row = ','.join(map(str, user_row))
        print(user_row)
        driver.find_element_by_xpath('//input[@id="user_first_name"]').send_keys(fname)
        driver.find_element_by_xpath('//input[@id="user_last_name"]').send_keys(lname)
        driver.find_element_by_xpath('//input[@id="user_email"]').send_keys(mail)
        driver.find_element_by_xpath('//input[@id="user_password"]').send_keys(password)
        driver.find_element_by_xpath('//input[@id="user-birthday-month"]').send_keys(month)
        driver.find_element_by_xpath('//input[@id="user-birthday-day"]').send_keys(day)
        driver.find_element_by_xpath('//input[@id="user-birthday-year"]').send_keys(year)

        try:
            wait = WebDriverWait(driver, 300)
            wait.until(lambda driver: driver.current_url != "https://do512.com/users/sign_up")
            print('register success')
            f = open("users.csv", "a")
            f.write(user_row+"\n")
            f.close()

            if ij == NO_OF_ACCOUNT_TO_BE_CREATED:
                return True
            else:
                ij+=1
                loadsite()
            

        except Exception as e:
            print("Waiting for Unsussfull, Reattempting")
            loadsite()
    
    except Exception as e:
        driver.refresh()
        loadsite()




CHROME_PROFILE_PATH = 'C:\\selenium\\prof1'
NO_OF_ACCOUNT_TO_BE_CREATED = 50


NO_OF_ACCOUNT_TO_BE_CREATED = input('Enter no of account to be created: ')
if NO_OF_ACCOUNT_TO_BE_CREATED == '':
    print('Enter no of account to be created')
    exit()


print('\nTotal '+str(NO_OF_ACCOUNT_TO_BE_CREATED)+' accounts will get created')
ij=1

options = Options()
prefs = {
        "profile.default_content_settings.popups" : 0,
        "directory_upgrade": True,
        "extensions_to_open": "",
        "safebrowsing.enabled": "false"
    }
options.add_experimental_option("prefs", prefs)
options.add_argument("--enable-easy-off-store-extension-install")
options.add_argument("user-data-dir="+str(CHROME_PROFILE_PATH)) #Path to your chrome profile
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
print("options added for chrome")
driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)
#exit()
loadsite()
    
driver.quit()
#os.system('scrap.exe')
