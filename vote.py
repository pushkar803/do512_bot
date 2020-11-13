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
def loadsite(email, password) :
    global driver,ij,LINK_OF_EVENT,ACTION
    
    print("Loading site started..........")
    #driver.maximize_window()
    print('Logging out...')
    print('\nLogging New User no '+str(ij))
    driver.get('https://do512.com/users/sign_out')
    sleep(4)
    driver.get("https://do512.com/users/sign_in")
    print("Wbsite login link called")
    print("Waiting for output from website...")
    
    sleep(4)
    
    # Check if the webpage is correctly loaded
    try:
        print(email)
        driver.find_element_by_xpath('//input[@id="user_email"]').send_keys(email)
        driver.find_element_by_xpath('//input[@id="user_password"]').send_keys(password)
        sleep(1)
        driver.find_element_by_xpath('//button[@class="ds-btn ds-btn-medium"]').click()

        try:
            wait = WebDriverWait(driver, 6)
            wait.until(lambda driver: driver.current_url != "https://do512.com/users/sign_in")
            print('login success')
            driver.get(LINK_OF_EVENT)
            if ACTION == 'upvote':
                vote_class = 'ds-btn stretch ds-btn-large ds-btn-ical ds-follow'
            elif ACTION == 'downvote':
                vote_class = 'ds-btn stretch ds-btn-large ds-btn-ical ds-follow upvoted'
            wait.until(lambda x: x.find_element_by_xpath('//a[@class="'+vote_class+'"]'))
            sleep(1)
            driver.find_element_by_xpath('//a[@class="'+vote_class+'"]').click()
            print(ACTION+' Successfully')
            sleep(1)
        except Exception as e:
            print("login Unsuccess...")
            #loadsite(email, password)
    
    except Exception as e:
        driver.refresh()
        loadsite(email, password)

CHROME_PROFILE_PATH = 'C:\\selenium\\prof1'
ACTION = input('Enter ACTION upvote or downvote: ')    #upvote or downvote
if ACTION != 'upvote':
    if ACTION != 'downvote':
        print('ENTER ACTION CORRECTLY i.e upvote or downvote')
        exit()
LINK_OF_EVENT = input('Enter link of event: ')
if LINK_OF_EVENT == '':
    print('ENTER LINK OF EVENT')
    exit()


ij = 0
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

data = pd.read_csv("users.csv", header=None)
total_users = len(data[0])
print('total user in files are '+str(total_users))
for i in range(0,total_users):
    ij = i+1
    email = data[0][i]
    password = data[1][i]
    loadsite(email, password)
    
driver.quit()
#os.system('scrap.exe')
