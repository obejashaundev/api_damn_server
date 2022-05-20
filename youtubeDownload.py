import json
from matplotlib.font_manager import json_dump
import youtube_dl

class YoutubeDownload():

    def downloadMp3(self, link, title, device):
        
        if "app" in device:
            #For youtube_dl
            ydl_opts = {
                'format': 'bestaudio',
                'keepvideo':False,
                'outtmpl': f"music/{title}.mp3",
                'noplaylist' : True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                file = open(title+".mp3", 'rb')
                lines = list()
                for line in file.readlines():
                    lines += list(line)
                file.close()
                file = {
                    "title": title,
                    "bytes": lines
                }
                return file
        elif "pwa" in device:
            #For youtube_dl
            ydl_opts = {
                'format': 'bestaudio',
                'keepvideo':False,
                'outtmpl': f"music/{title}.%(ext)s",
                'noplaylist' : True,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                file = title+".webm"
                return file
        
        # For pytube3
        #yt = YouTube(link)
        #return yt.streams.filter(only_audio=True)


# Test!!

#YoutubeDownload().downloadMp3('https://www.youtube.com/watch?v=nTgWUUT6fFM','')

#ask for the link from user
#link = input("Enter the link of YouTube video you want to download:  ")


#Starting download
#print("Downloading...")
#ys.download()
#print("Download completed!!")