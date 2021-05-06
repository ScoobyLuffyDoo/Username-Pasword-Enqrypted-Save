import services.encryptionModule as encrypt


username ='2317'
strength =35
# Encryption Serice 
encryptedString = encrypt.stringEncrypt(username,strength)
print(encryptedString)
print(len(encryptedString))
#  Decryption Service
decryptedString = encrypt.strinDecrypt(encryptedString,strength)
print(decryptedString)