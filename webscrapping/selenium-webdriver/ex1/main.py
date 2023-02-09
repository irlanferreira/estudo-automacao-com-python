import time
from selenium import webdriver

navegador = webdriver.Edge()
navegador.set_window_size(1920, 1080)
navegador.get('https://unsplash.com')
barrapesquisa = navegador.find_element('name', 'searchKeyword')
barrapesquisa.send_keys('sky')
barrapesquisa.submit()
time.sleep(30)