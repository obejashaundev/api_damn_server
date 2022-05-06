
import re

from crypt import methods
from flask import Flask, jsonify, request
from api import YoutubeAPISearch
from youtubeDownload import YoutubeDownload
from DataEncrypt import DataEncrypt
from DataDecrypt import DataDecrypt
from database import ConnectToDatabase

yas = YoutubeAPISearch(APIKey='AIzaSyB5lvaMBDh6Js8twjSDa8hKLf-MQx_AkuI')
yd = YoutubeDownload()
app = Flask(__name__)
db = ConnectToDatabase()
encryptor = DataEncrypt()
decryptor = DataDecrypt()

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

    if ("@" in email) and len(password) >= 8:
        #USE ANY API TO VALIDATE EMAIL FOR CHECK IF IS REAL EMAIL.
        print(f'email => {email}')
        print(f'password => {password}')

        # TO DO encrypt password and email
        encryptor.setStringToEncrypt(password)
        password_encrypted = encryptor.encrypt()
        db.addNewUser(email,password_encrypted)
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
            decryptor.setStringToDecrypt(dbAccessToken)
            #Test
            '''
            print(dbEmail)
            print(dbAccessToken)
            '''
            if (dbEmail == email) and decryptor.decrypt():
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