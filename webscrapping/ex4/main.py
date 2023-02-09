from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import random
def setaaleatoria(nav):
    num = random.randint(1, 4)
    match num:
        case 1:
            return nav.send_keys(Keys.LEFT)
        case 2:
            return nav.send_keys(Keys.UP)
        case 3:
            return nav.send_keys(Keys.RIGHT)
        case 4:
            return nav.send_keys(Keys.DOWN)

nav = webdriver.Edge()
nav.get('https://play2048.co')
htmlelement = nav.find_element('tag name', 'html')
while True:
    setaaleatoria(htmlelement)
    time.sleep(0.4)
    try:
        tentardnv = nav.find_element('css selector', 'a.retry-button')
        tentardnv.click()
    except:
        continue