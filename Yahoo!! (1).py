from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import pynput
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
from pynput.keyboard import Key, Controller
import pyautogui 
from keyboard import press		

abc='Pralay Sarkar'
zz='https://in.yahoo.com/'
driver = webdriver.Chrome("C:/Users/Anushree Khan/Downloads/chromedriver_win32/chromedriver")

driver.get(zz)
time.sleep(0.5)
search = driver.find_element_by_xpath('//*[@id="header-search-input"]')
search.send_keys(abc,Keys.ENTER)
time.sleep(2)
#for a in driver.find_elements_by_xpath('.//a'):
#    print(a.get_attribute('href'))

    
