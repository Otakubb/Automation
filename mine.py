import pyautogui as pag
from time import sleep

sleep(10)
pag.mouseDown()
pag.keyDown('w')

pag.FAILSAFE = True
