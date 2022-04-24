from crypt import methods
from flask import Flask, jsonify, request
from api import YoutubeAPISearch
from youtubeDownload import YoutubeDownload

from database import ConnectToDatabase

yas = YoutubeAPISearch(APIKey='AIzaSyB5lvaMBDh6Js8twjSDa8hKLf-MQx_AkuI')
yd = YoutubeDownload()
app = Flask(__name__)
db = ConnectToDatabase()

@app.route('/signUp', methods=['POST'])
def signUp():
    email = request.json['email']
    password = request.json['password']
    ok = False

    # Test
    '''
    print(email)
    print("@ in email: ")
    print("@" in email)
    print(password)
    print("len(password): ")
    print(len(password))
    '''

    # TO DO encrypt password and email
    if ("@" in email) and len(password) >= 8:
        db.addNewUser(email,password)
        ok = True
    return jsonify({
        "result": f"{ok}"
    })

@app.route('/signIn', methods=['POST'])
def signIn():
    email = request.json['email']
    password = request.json['password']
    if ("@" in email) and (len(password) >= 8):
        id = db.getIdUser(email)
        #Test
        #print("id: "+str(id))
        if (id != -1):
            dbEmail, dbAccessToken = db.getCredentials(id)
            #Test
            '''
            print(dbEmail)
            print(dbAccessToken)
            '''
            if (dbEmail == email) and (dbAccessToken == password):
                return jsonify({
                    "result": "authorized"
                })
    return jsonify({
        "result": "unauthorized"
    })

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