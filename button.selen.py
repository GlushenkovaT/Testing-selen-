from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/')

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/')

xpath = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button'
browser.find_element_by_xpath(xpath).click()

from_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
browser.find_element_by_xpath(from_xpath).send_keys('0935211432')
