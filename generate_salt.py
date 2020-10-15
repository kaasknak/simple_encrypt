import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def write_key(nameFile, key):
    with open(nameFile, "wb") as key_file:
        key_file.write(key)

#Generates the salt and prints it before saving it as salt.key
salt = os.urandom(16)
print(salt)
write_key("salt.key", salt)
