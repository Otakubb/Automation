import pyautogui
import time
import datetime

while 1 == 1:  # isto é um loop enquanto 1 for igual a 1 ele vai fazer isto que esta aqui embaixo....como 1 sempre vai ser igual a 1 ele vai faqzer isto infinitamente
    pyautogui.click(64, 759)  # clica naquela coordnada(coordenada do meu disc na barra de tarefas
    time.sleep(2)  # espera 2s
    pyautogui.click(395, 677)  # clica naquela coordenada (coordenada o campo de escrever msg)
    time.sleep(1)  # espera 1s
    for i in range(1, 9):  # isto é tipo um loop de 8vezes
        pyautogui.write('$wa')  # escreve $wa
        pyautogui.press('enter')  # carrega no enter
        time.sleep(6)  # pausa durante 6s
    time.sleep(3600)  # pausa durante 1h
