import os
from dotenv import load_dotenv
import pymysql

class ConnectToDatabase():

    def __init__(self):
        load_dotenv()
        self.__connection = pymysql.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
    
    def addNewUser(self,email,password):
        with self.__connection.cursor() as cursor:
            query = "INSERT INTO credentials (email,access_token) VALUES(%s,%s);"
            cursor.execute(query,(email,password))
        self.__connection.commit()
            #self.__connection.close()
    
    def getIdUser(self, email):
        id = -1
        try:
            with self.__connection.cursor() as cursor:
                query = "SELECT id FROM credentials WHERE email=%s"
                cursor.execute(query, (email))
                result = cursor.fetchall()
                id = result[0][0]
            self.__connection.commit()
        finally:
            #self.__connection.close()
            return id

    def getCredentials(self, id):
        credentials = {
            "email": '',
            "access_token": ''
        }
        try:
            with self.__connection.cursor() as cursor:
                query = "SELECT email,access_token FROM credentials WHERE id=%s"
                cursor.execute(query, (id))
                result = cursor.fetchall()
                credentials["email"] = result[0][0]
                credentials["access_token"] = result[0][1]
            self.__connection.commit()
        finally:
            #self.__connection.close()
            return credentials["email"],credentials["access_token"]

    def addHistory(self, idUser, keyword):
        with self.__connection.cursor() as cursor:
            query = f"INSERT INTO history (user,registry) VALUES({idUser},{keyword});"
            cursor.execute(query)
        self.__connection.commit()
            #self.__connection.close()

    def getUserHistory(self, idUser):
        allHistory = []
        try:
            with self.__connection.cursor() as cursor:
                query = f"SELECT registry FROM history WHERE user={idUser}"
                cursor.execute(query)
                allHistory = cursor.fetchall()
            self.__connection.commit()
        finally:
            #self.__connection.close()
            return allHistory

'''id = ConnectToDatabase().getIdUser("obed@gmail.com")
print(id)'''