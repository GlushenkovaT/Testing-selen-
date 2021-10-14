from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/')
html = browser.find_element_by_tag_name('html')
for i in range(10):
	html.send_keys(Keys.DOWN)



option.headless = True