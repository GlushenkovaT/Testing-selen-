import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument ('--proxy-server=192.168.0.190')
browser = webdriver.Chrome (options=option)
browser.get('https://icanhazip.com')