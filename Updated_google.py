from selenium import webdriver 
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import pynput
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
#------------------------>input string
abc='Pralay Sarkar'
zz='https://www.google.co.in/webhp'
driver = webdriver.Chrome("c:/Users/soham/Downloads/chromedriver_win32/chromedriver")

driver.get(zz)

time.sleep(0.5)
search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys(abc,Keys.ENTER)
time.sleep(2)
#for a in driver.find_elements_by_xpath('.//a'):
#    print(a.get_attribute('href'))
        
#//*[@id="rso"]/div[1]/div/div[1]/a/h3
#//*[@id="rso"]/div[2]/div/div[1]/a/h3
#//*[@id="rso"]/div[3]/div/div[1]/a/h3
##rso > div:nth-child(1) > div > div.r > a > h3
i=1
print("#rso > div:nth-child("+str(i)+") > div > div.r > a > h3")
while(1):
    driver.find_element_by_css_selector("#rso > div:nth-child("+str(i)+") > div > div.r > a > h3").click()
    time.sleep(0.5)
    url = driver.current_url
    driver.get(url)

    time.sleep(2)
    dd=driver.find_element_by_xpath("//body").text
    print(dd)
    cc=str(dd)
    try:
        file_object  = open("output_google_search.txt",'a+')
        file_object.write(cc)
        file_object.close()
        driver.execute_script("window.history.go(-1)")
        i=i+1
    except:
        driver.execute_script("window.history.go(-1)")
        i=i+1

