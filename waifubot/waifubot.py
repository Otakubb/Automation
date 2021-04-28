import pyautogui
import time
import datetime

img = pyautogui.locateOnScreen('channel2.png')
while 1 == 1:

    hora = datetime.datetime.now()
    if hora.minute < 10:
        print('{}:0{}'.format(hora.hour, hora.minute))
    else:
        print('{}:{}'.format(hora.hour, hora.minute))

    pyautogui.click(64, 759)
    time.sleep(2)

    if img != None:
        pyautogui.click('channel2.png')
    else:
        pyautogui.click('171, 379')
        
    pyautogui.click(395, 677)
    time.sleep(1)

    for i in range(1, 9):
        pyautogui.write('$wa')
        pyautogui.press('enter')
        time.sleep(1.5)
        
    time.sleep(3600)

    pyautogui.click('16, 756')
    
