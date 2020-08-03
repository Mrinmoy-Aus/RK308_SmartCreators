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
import codecs
abc='Pralay Sarkar'
zz='https://www.google.co.in/webhp'
driver = webdriver.Chrome("C:/Users/Anushree Khan/Downloads/chromedriver_win32/chromedriver")
driver.get(zz)
time.sleep(0.5)
search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys(abc,Keys.ENTER)
time.sleep(2)
i=1
while(1):
    driver.find_element_by_css_selector("#rso > div:nth-child("+str(i)+") > div > div.r > a > h3").click()
    url = driver.current_url
    driver.get(url)
    print(url)
    dd=driver.find_element_by_xpath("//body").text
    print(dd)
    cc=str(dd)
    file_object  = codecs.open("output_google.txt","a","utf-8")
    file_object.write(cc)
    file_object.close()

    time.sleep(0.5)
    driver.execute_script("window.history.go(-1)")
    i=i+1

