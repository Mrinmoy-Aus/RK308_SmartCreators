from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2
i=1
cc='https://twitter.com/mrinmoy_aus'
r = requests.get(cc)
print(cc)
j=str(i)
s = BeautifulSoup(r.text,"html.parser")
a=(cc)
print(a)
p = s.find("meta",property ="og:image").attrs['content']
with open(j+".jpg","wb") as pic:
        binary = requests.get(p).content
        pic.write(binary)
