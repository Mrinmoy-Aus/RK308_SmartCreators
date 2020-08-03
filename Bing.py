from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import pynput
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2	
#---------------------input string

abc='mrinmoy aus'
zz='https://www.bing.com/'
driver = webdriver.Chrome("c:/Users/soham/Downloads/chromedriver_win32/chromedriver")

driver.get(zz)
time.sleep(0.5)
search = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
search.send_keys(abc,Keys.ENTER)
time.sleep(2)

i=2
print("#b_results > li:nth-child("+str(i)+") > h2 > a")
while(1):
    driver.find_element_by_css_selector("#b_results > li:nth-child("+str(i)+") > h2 > a").click()
    time.sleep(0.5)
    url = driver.current_url
    driver.get(url)

    time.sleep(2)
    dd=driver.find_element_by_xpath("//body").text
    print(dd)
    cc=str(dd)
   
    try:
        file_object  = open("output_bing_search.txt",'a+')
        file_object.write(cc)
        file_object.close()
        driver.execute_script("window.history.go(-1)")
        i=i+1
        
    except:
        driver.execute_script("window.history.go(-1)")
        i=i+1
    
