from cryptography.fernet import Fernet
import binascii

# Loads Encryption Key 
# This key will be stored in a mongo instance 
def loadkey():
    """ Loads the key from the current directory"""
    return open("key.key","rb").read()

# Encryption Function 
def stringEncrypt(inputstring,strength):
    f = Fernet(loadkey())
    inputstring = bytes(inputstring, 'utf8')
    print(inputstring)
    # encrypt the  string
    encryptedString = inputstring
    for i in range(strength):
        encryptedString = f.encrypt(encryptedString)
    return encryptedString

    
# Decryption Function
def strinDecrypt(inputstring,strength):
    f = Fernet(loadkey())
    # decrypt the file
    encrypted_string =inputstring
    for i in range(strength):
        encrypted_string = f.decrypt(encrypted_string)
    return encrypted_string
