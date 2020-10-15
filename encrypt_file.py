import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

def load_file(fileName):
    return open(fileName, "rb").read()

def write_file(fileName, toSave):
    with open(fileName, "wb") as key_file:
        key_file.write(toSave)

#Password is required in order to construct the key.
print("Input password:")
password=getpass()
password=password.encode()
salt = load_file("salt.key")
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1000000,)
key = base64.urlsafe_b64encode(kdf.derive(password))
f=Fernet(key)

#The file to encrypt is requested.
print("Which file do you want to encrypt?")
encryptFile=input()
clearFile=load_file(encryptFile)
try:
    encr=f.encrypt(clearFile)
    print("What do you want to call the encrypted file?")
    fileName=input()
    write_file(fileName, encr)
except:
    print("Something went wrong and the file has not been encrypted.")
