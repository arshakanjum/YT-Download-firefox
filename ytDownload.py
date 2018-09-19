import os, json, lz4.block,sys
import re
from youtube_dl import YoutubeDL
f = open("C:\Users\I353363\AppData\Roaming\Mozilla\Firefox\Profiles\\3flzkmuc.default\sessionstore-backups\\recovery.jsonlz4", "rb")
magic = f.read(8)
jdata = json.loads(lz4.block.decompress(f.read()).decode("utf-8"))
f.close()
for win in jdata.get("windows"):
    for tab in win.get("tabs"):
        i = tab.get("index") - 1
        urls = tab.get("entries")[i].get("url")
        if urls.find('youtube')!=-1:
            code= re.split('watch\?v=|&',urls)[1].encode('utf8')
            
            if len(sys.argv) > 1:
                 ydl_opts={'format':'mp4',
                          'outtmpl': '/YTDownloads/Videos/%(title)s.%(ext)s'}
            else:
                ydl_opts = {'format': 'bestaudio/best',
                            'no_warnings': True,
                            'outtmpl': '/YTDownloads/Audios/%(title)s.%(ext)s',
                            'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            }],}
            ydl = YoutubeDL(ydl_opts)

            ydl.download([code])
            