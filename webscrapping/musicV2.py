from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyautogui as pag

#########################################################

musicname = str(input('Nome da musica:'))

PATH = "/home/santi/Documentos/workspace/chromedriver"
driver = webdriver.Chrome(PATH)

#img = locateOnScreen('Agree.png')
youtube = 'https://www.youtube.com'

driver.get(youtube)

sleep(5)
#########################################################
size = pag.size()

size = str(size)

size = size.replace(',', ' ')
size = size.replace('=', ' ')
size = size.replace(')', ' ')

size = size.split(' ')

szx = size[1]
szy = size[4]

szx = int(szx)
szy = int(szy)

midx = szx/2
midy = szy/2

midx = str(midx)
midy = str(midy)

midx = midx.replace('.0', '')
midy = midy.replace('.0', '')

midx = int(midx)
midy = int(midy)

pag.moveTo(midx, midy)
#########################################################
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

#url = 'https://ytmp3.cc/youtube-to-mp3/'
#site = driver.get(url)
 
#txtbox = driver.find_element_by_id('input')
#txtbox.send_keys(musiclink)
#txtbox.send_keys(Keys.RETURN)

#driver.implicitly_wait(25)

#download = driver.find_element_by_link_text('Download')
#download.click()
