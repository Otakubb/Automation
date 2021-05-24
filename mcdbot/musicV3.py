
import requests
from youtube_dl import YoutubeDL

# By Feh's

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

info = search(input('Nome da música: ').replace(' ', '+'))

print(info)

#By Ota's

import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([info])
