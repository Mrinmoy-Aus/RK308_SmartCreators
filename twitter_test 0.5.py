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
keyboard = Controller()
abc=' '
a='mrinmoy' ######### input ###########
b='aus'     ######### input ###########
                
cc='https://twitter.com/search?q=%20'
dd='%20'
ee='&src=typed_query&f=user'
zz=str(cc)+str(a)+str(dd)+str(b)+str(ee)
print(zz)
#print the total page link
driver = webdriver.Chrome("c:/Users/soham/Downloads/chromedriver_win32/chromedriver")

driver.get(zz)
time.sleep(2)
i=1
while(True):
    print("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div > div > div > div > div > div > section > div > div > div > div:nth-child("+str(i)+") > div > div")
    driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div > div > div > div > div > div > section > div > div > div > div:nth-child("+str(i)+") > div > div").click()
    time.sleep(1)
    
    i=i+1
    cc = driver.current_url
    print(cc)
    driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div > div > div > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-ku1wi2.r-1j3t67a.r-m611by > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1wtj0ep > a").click()
    time.sleep(1)
    driver.save_screenshot("profile_pic.png")
    driver.back()
    #######################
    ###    pic matcher  ###
    #######################
    ## My twitter scrap  ##
    
    #######################
    ##  else continue #####
    #######################
    time.sleep(0.5)
    driver.execute_script("window.history.go(-1)")
    
#
