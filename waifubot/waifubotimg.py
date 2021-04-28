import pyautogui
import time
import datetime

img1 = pyautogui.locateOnScreen('channel1.png')
img2 = pyautogui.locateOnScreen('channel2.png')
img3 = pyautogui.locateOnScreen('channel3.png')

while 1 == 1:

    hora = datetime.datetime.now()
    if hora.minute < 10:
        print('{}:0{}'.format(hora.hour, hora.minute))      #diz a que horas foi executado o cmd
    else:
        print('{}:{}'.format(hora.hour, hora.minute))

    pyautogui.click(64, 759)                 #clica no dc  
    time.sleep(2)

    if img1 != None:
        pyautogui.click('channel1.png')
    elif img2 != None:
        pyautogui.click('channel2.png')      #reconhece png do channel (marcado, com msg por ler, sem msg pra ler
    elif img3 != None:
        pyautogui.click('channel3.png')
        
    pyautogui.click(395, 677)               # clica no campo de msg
    time.sleep(1)

    for i in range(1, 9):
        pyautogui.write('$wa')
        pyautogui.press('enter')     #escreve as msg
        time.sleep(6)
        
    time.sleep(3600)                

    pyautogui.click('16, 756') #abre o opera para qnd clicar dnv no dc n fechar em vez de abrir

    
