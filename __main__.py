from crypt import methods
from flask import Flask, jsonify, request
from api import YoutubeAPISearch
from youtubeDownload import YoutubeDownload

yas = YoutubeAPISearch(APIKey='AIzaSyB5lvaMBDh6Js8twjSDa8hKLf-MQx_AkuI')
yd = YoutubeDownload()
app = Flask(__name__)

@app.route('/search/<something>')
def search(something):
    results = yas.searchSomething(text=something)
    return jsonify({
        "results": results
    })

@app.route('/download', methods=['POST'])
def download():
    link = request.json["link"]
    title = request.json["title"]
    print("title:   "+title+"   =>  "+link)
    file = yd.downloadMp3(link, title)
    return jsonify({
        "message": "File Transfer",
        "file": file
    })

if __name__ == '__main__':
    app.run(port=4000)