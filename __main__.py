
#from crypt import methods
from flask import Flask, jsonify, request, send_file, send_from_directory, abort
from flask_cors import CORS

from api import YoutubeAPISearch
from youtubeDownload import YoutubeDownload
from DataEncrypt import DataEncrypt
from DataDecrypt import DataDecrypt
from database import ConnectToDatabase

yas = YoutubeAPISearch()
yd = YoutubeDownload()
app = Flask(__name__)
CORS(app)
db = ConnectToDatabase()
encryptor = DataEncrypt()
decryptor = DataDecrypt()


app.config["CLIENT_MUSIC"] = "./music"

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
        print(f'password encrypted => {password_encrypted}')
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
    r = jsonify(results)
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r

@app.route('/downloadApp', methods=['POST'])
def downloadApp():
    link = request.json["link"]
    title = request.json["title"]
    file = yd.downloadMp3(link, title, 'app')
    return jsonify(file)

@app.route('/downloadPwa', methods=['GET'])
def downloadPwa():
    args = request.args
    titulo = args.get('titulo')
    url = args.get('url')
    file = yd.downloadMp3(url, titulo, 'pwa')
    try:
        return send_from_directory(app.config['CLIENT_MUSIC'], file, as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)