from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs 
import requests

musiclink = str(input('Link da musica\n->'))

PATH = "/home/santi/Documentos/workspace/chromedriver"
driver = webdriver.Chrome(PATH)

url = 'https://ytmp3.cc/youtube-to-mp3/'
site = driver.get(url)

txtbox = driver.find_element_by_id('input')
txtbox.send_keys(musiclink)
txtbox.send_keys(Keys.RETURN)

driver.implicitly_wait(25)

download = driver.find_element_by_link_text('Download')
download.click()

