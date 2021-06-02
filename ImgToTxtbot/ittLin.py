from typing import Text
from PIL import Image
import pytesseract
import getpass
import PySimpleGUI as sg

#layout-=-=-=-=-=
sg.theme('DarkAmber')
def janela():
    layout = [#layout da janela1

         [sg.Text('caminho da Imagem (incluindo o formato):')], 

         [sg.Input(key='img')],

         [sg.Button('Ler img')]

    ]
    return sg.Window('Read Image', layout, finalize=True)

def janela_txt():
    layout = [#layout da janela2

       [sg.Text('Erro. não foi possivel reconhecer o caminho\nou não foi possivel reconhecer o texto na imagem.', key='wtxt')],

       [sg.Button('voltar')]

    ]
    return sg.Window('Text', layout, finalize=True)

janela1, janela2 = janela(), None

while True:

    window, event, values = sg.read_all_windows()    

    if window == janela1 and event == sg.WIN_CLOSED :
        break #fecha a janela

    if window == janela1 and event == 'Ler img': 

        text = pytesseract.image_to_string(values['img']) #dá um valor ao text
        janela2 = janela_txt()
        janela1.hide()


    try:
        janela2.Element('wtxt').update('O seu texto foi escrito no terminal') #mostra que o texto foi escrito no terminal
        print('=-'*25)
        print(text)
        print('=-'*25)
    except:
        pass

    if window == janela2 and event == sg.WIN_CLOSED :
        break #fechar na janela2

    if window == janela2 and event == 'voltar':

        janela2.hide()
        janela1.un_hide()   #esconde uma janela e faz a outra aparecer