import time
from selenium import webdriver

option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override','example :)')
browser = webdriver.Firefox(options=option)
browser.get ('https://ciox.ru/check-user-agent')