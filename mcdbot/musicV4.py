import PySimpleGUI as sg

#layout==-==-==-==-==-==-==-==-
sg.theme('DarkAmber')
layout = [

            [sg.Text('Música:'),sg.Input(key='musica')],

            [sg.Button('Baixar')]

    ]
#janela==-==-==-==-==-==-==-==-
janela = sg.Window('Download Music', layout)

#eventos==-==-==-==-==-==-==-==-
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Baixar':
        
        import requests
        from youtube_dl import YoutubeDL
        
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        def search(arg):
            with YoutubeDL(YDL_OPTIONS) as ydl:
                try:
                    requests.get(arg) 
                except:
                    video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
                else:
                    video = ydl.extract_info(arg, download=False)

            return video['webpage_url']

        valores['musica'] == str(valores['musica']).replace(' ','+')

        import youtube_dl
        
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([valores['musica']])

