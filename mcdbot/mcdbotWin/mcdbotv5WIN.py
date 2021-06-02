#este ficheiro tem de estar localizaado em transferencias para funcionar
from tkinter import Checkbutton
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Checkbox
import os
import platform
import getpass
import shutil

user = getpass.getuser()

#layout==-==-==-==-==-==-
sg.theme('DarkAmber')
layout = [

            [sg.Text('Idioma do seu pc:')],

            [sg.Checkbox('pt', key='pt'), sg.Checkbox('eng', key='eng')],

            [sg.Text('Música:'),sg.Input(key='musica')],

            [sg.Button('Baixar')],

            [sg.Text('Se pretender baixar mais que uma música,\nreescreva no campo "música"')]

        ]
#janela==-==-==-==-==-==-==-
janela = sg.Window('Download Music', layout,  icon='Logo2.png')

#eventos==-==-==-==-==-==-==-==-
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Baixar':
        
        import requests
        from youtube_dl import YoutubeDL
       
        YDL_OPTIONS = { 
            'outtmpl': 'downloaded_music/%(title)s.%(ext)s',
            'format': 'm4a', 
            'noplaylist': 'True'
        }

        def search(arg):
            with YoutubeDL(YDL_OPTIONS) as ydl:
                try:
                    requests.get(arg) 
                except:
                    video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
                    print('====================================================\n{}\n===================================================='.format(video['title']))
                    search.title = video['title']
                else:
                    video = ydl.extract_info(arg, download=False)
                
                ydl.download([video['webpage_url']])
                
            
            return video


        valores['musica'] == str(valores['musica']).replace(' ','+')
        
        search(valores['musica'])

        sis = str(platform.platform()).replace('-', ' ').split()[0]
                     
        if sis == 'Windows':
            
            original = r'C:\Users\{}\Downloads\mcdbotWin\downloaded_music\{}.m4a'.format(user, search.title)
            target = r'C:\Users\{}\Music'.format(user)

            shutil.move(original,target)
