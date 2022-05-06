import bcrypt

class DataDecrypt:
    def __init__(self, dataEncrypted=''):
        self.string_encrypted = "{}".format(dataEncrypted)
        self.string_encrypted = self.string_encrypted.encode('utf-8')
        
        
    def decrypt(self, number_of_rounds=16):
        salt = bcrypt.gensalt(rounds=number_of_rounds)
        hash_str = bcrypt.hashpw(self.string_encrypted, salt)
        if bcrypt.checkpw(self.string_encrypted, hash_str):  
            return True  
        else:  
            return False  
    
    def setStringToDecrypt(self, hashh):
        self.string_encrypted = "{}".format(hashh)
        self.string_encrypted = self.string_encrypted.encode('utf-8')