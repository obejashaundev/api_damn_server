import os
from dotenv import load_dotenv

from copyreg import constructor
from tokenize import String
import requests
import json

load_dotenv()

class YoutubeAPISearch():
    

    def __init__(self, APIKey=os.getenv('APIKey')) -> None:
        self.APIKey = APIKey

    def searchSomething(self, text):
        searchText = text.replace(" ","+")
        result = self.__requestYoutube(searchText)
        jsonResult = json.loads(result)
        return self.__formatOutputSearch(jsonResult)

    def __requestYoutube(self,something):
        #self.rawJSON = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyB5lvaMBDh6Js8twjSDa8hKLf-MQx_AkuI&type=video&q='+self.searchText+'&maxResults=10')
        rawJSON = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&key='+self.APIKey+'&type=video&q='+something+'&maxResults=10')
        return rawJSON.text
    
    def __formatOutputSearch(self, json):
        items = json['items']
        resultVideos = []
        for videoItem in items:
            videoId = videoItem['id']['videoId']
            video = {
                "title": videoItem['snippet']['title'],
                "url": 'https://www.youtube.com/watch?v='+videoId,
                "thumbnailURL": videoItem['snippet']['thumbnails']['high']['url']
            }
            resultVideos.append(video)
        return resultVideos