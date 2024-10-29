from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def key_deriver(user_key, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(user_key.encode())

def encrypter(input_file, user_key):
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = key_deriver(user_key, salt)
    
    with open(input_file, 'r') as file:
        passwords = file.readlines()

    encrypted_passwords = []
    for password in passwords:
        password = password.strip().encode()
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted = encryptor.update(password) + encryptor.finalize()
        encrypted_passwords.append((salt, nonce, encryptor.tag, encrypted))

    output_file = os.path.join(os.path.dirname(input_file), "encrypted_passwords.txt")
    with open(output_file, 'wb') as file:
        for salt, nonce, tag, encrypted in encrypted_passwords:
            file.write(salt + nonce + tag + encrypted + b'\n')

    print(f"Encrypted passwords have been saved to {output_file}")

def decrypter(input_file, user_key):
    decrypted_passwords = []
    with open(input_file, 'rb') as file:
        lines = file.readlines()

    for line in lines:
        salt = line[:16]
        nonce = line[16:28]
        tag = line[28:44]
        encrypted = line[44:].strip()
        key = key_deriver(user_key, salt)

        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        try:
            decrypted = decryptor.update(encrypted) + decryptor.finalize()
            decrypted_passwords.append(decrypted.decode())
        except Exception as e:
            print(f"Error decrypting password (Check the User Key): {e}")
            print(f"Salt: {salt}\nNonce: {nonce}\nTag: {tag}\nEncrypted: {encrypted}")
            return

    output_file = os.path.join(os.path.dirname(input_file), "decrypted_passwords.txt")
    with open(output_file, 'w') as file:
        for decrypted in decrypted_passwords:
            file.write(decrypted + '\n')

    print(f"Decrypted passwords have been saved to {output_file}")

ops = input("Do you want to (e)ncrypt or (d)ecrypt the file? ").strip().lower()
key = input("Enter the encryption key: ")
file = input("Enter the path to the file without the double quotes: ")

if ops == 'e':
    encrypter(file, key)
elif ops == 'd':
    decrypter(file, key)
else:
    print("Invalid option. Please choose 'e' to encrypt or 'd' to decrypt.")
