import PySimpleGUI as sg

#layout==-==-==-==-==-==-
sg.theme('DarkAmber')
layout = [

            [sg.Text('Música:'),sg.Input(key='musica')],

            [sg.Button('Baixar')]

    ]
#janela==-==-==-==-==-==-==-
janela = sg.Window('Download Music', layout)

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
                else:
                    video = ydl.extract_info(arg, download=False)
                
                ydl.download([video['webpage_url']])
            
            return video


        valores['musica'] == str(valores['musica']).replace(' ','+')
        
        search(valores['musica'])
