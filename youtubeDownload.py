import youtube_dl

class YoutubeDownload():

    def __my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    def downloadMp3(self, link, title):
        
        #For youtube_dl
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': title+".%(ext)s",        
            'noplaylist' : True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            file = open(title+".webm", 'rb')
            lines = ''
            for line in file.readlines():
                lines += str(line)
            file.close()
            file = {
                "title": title,
                "bytes": lines
            }
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