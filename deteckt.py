import time
from selenium import webdriver

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled',False)
option.set_preference('dom.webnotification.enabled',False)
option.set_preference('media.volume_scale','0.0')
option.headless = True

browser = webdriver.Firefox(options=option)
browser.get('https://nick-name.ru/generate/')

while True:
	button_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
	browser.find_element_by_xpath(button_xpath).click()

	#извлекаем ник-нейм
	link = browser.find_element_by_id('register').get_attribute('href')[36:]
	print(f'Nickname:{link}')