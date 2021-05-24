from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyautogui as pag

#########################################################

musicname = str(input('Nome da musica:'))

PATH = "/home/santi/Documentos/workspace/chromedriver"
driver = webdriver.Chrome(PATH)

img = pag.locateOnScreen('Agree.png')
youtube = 'https://www.youtube.com'

driver.get(youtube)

sleep(5)

sleep(3)

agree = pag.click(img)

sleep(10)

search = driver.find_element_by_id('search')
search.send_keys(musicname)
search.send_keys(Keys.RETURN)

sleep(10)

thumb = driver.find_element_by_id('thumbnail')
musiclink = thumb.get_attribute('href')
print(musiclink)
#########################################################
pag.scroll(3)
#########################################################

#url = 'https://ytmp3.cc/youtube-to-mp3/'
#site = driver.get(url)
 
#txtbox = driver.find_element_by_id('input')
#txtbox.send_keys(musiclink)
#txtbox.send_keys(Keys.RETURN)

#driver.implicitly_wait(25)

#download = driver.find_element_by_link_text('Download')
#download.click()
