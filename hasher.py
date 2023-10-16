import rsa
from os.path import exists
import random as rnd

BASE_DIR = "./keys/.privateKey.pem"

public_key_exists = exists("./keys/.publicKey.pem")
private_key_exists = exists("./keys/.privateKey.pem")


if public_key_exists == True and private_key_exists == True :
    print("Printing Keys")
    with open("./keys/.publicKey.pem", 'rb') as p:
        PUBLIC_KEY = rsa.PublicKey.load_pkcs1(p.read())

    with open("./keys/.privateKey.pem", 'rb') as p:
        PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(p.read())

else:
    print("Generating Keys")
    (publicKey, privateKey) = rsa.newkeys(512)

    with open("./keys/.publicKey.pem", 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    
    with open("./keys/.privateKey.pem", 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))
    
    with open("./keys/.publicKey.pem", 'rb') as p:
        PUBLIC_KEY = rsa.PublicKey.load_pkcs1(p.read())

    with open("./keys/.privateKey.pem", 'rb') as p:
        PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(p.read())


def HashPassword(password):
    encrypted_password = rsa.encrypt(password.encode('utf-8'),PUBLIC_KEY)
    return encrypted_password

def UnhashPassword(hashedPass):
    decrypted_password = rsa.decrypt(hashedPass,PRIVATE_KEY).decode('utf-8')    
    return decrypted_password

def GeneratePassword():
    CHARS = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890@#$%*()_-+="
    new_password = ''
    for i in range(0,13):
        a = rnd.choice(CHARS)
        new_password += a
    return new_password