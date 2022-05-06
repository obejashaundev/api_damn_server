import bcrypt

class DataEncrypt:
    def __init__(self, plainData=''):
        self.string_to_encrypt = "{}".format(plainData)
        self.string_to_encrypt = self.string_to_encrypt.encode('utf-8')
    
    def encrypt(self, number_of_rounds=16):
        salt = bcrypt.gensalt(rounds=number_of_rounds)
        hashed_string = bcrypt.hashpw(self.string_to_encrypt, salt)
        return hashed_string

    def setStringToEncrypt(self, text):
        self.string_to_encrypt = "{}".format(text)
        self.string_to_encrypt = self.string_to_encrypt.encode('utf-8')
