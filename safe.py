import os
from cryptography.Fernet import Fernet

files = []

for file in os.listdir():
  if file == "supersafe.py" or file == "thekey.key" or file == "safe.py":
    continue
  if os.path.isfile(file):
    files.append(file)


with open("thekey.key", "rb") as thekey:
  key = thekey.read()

for file in files:
  with open(file, "rb") as thefile:
    contents_encrypted = thefile.read()
  contents_decrypted = Fernet(key).decrypt(contents_encrypted)
  with open(file, "wb") as thefile:
    thefile.write(contents_decrypted)
