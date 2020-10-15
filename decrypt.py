import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

#Load the keyfile
def load_key(fileName):
    return open(fileName, "rb").read()

#Password for decrytion
print("Input password:")
password=getpass()
password=password.encode()
#Loading of salt, construction of key.
salt = load_key("salt.key")
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1000000,)
key = base64.urlsafe_b64encode(kdf.derive(password))
f=Fernet(key)

print("Which file do you want to decrypt?")
fileName=input()
#Actual decryption. It will print the decrypted file (if the key is correct).
try:
    encryp=load_key(fileName)
    decr=f.decrypt(encryp)
    print(decr.decode())
except:
    print("Wrong password or wrong salt or maybe the file doesn't even exist.....")
