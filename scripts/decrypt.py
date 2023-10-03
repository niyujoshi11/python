import os
from cryptography.fernet import Fernet

# Function to generate a new Fernet key and save it to a file
def generate_and_save_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)

# Function to decrypt files using the provided key
def decrypt_files(key_file, files):
    if not os.path.exists(key_file):
        print("No key found. Generating a new key.")
        generate_and_save_key(key_file)
        print("Key has been generated and saved as 'thekey.key'.")
    
    with open(key_file, "rb") as key:
        secretkey = key.read()

    # Replace 'your_fixed_passphrase' with your actual passphrase
    secretphrace = 'your_fixed_passphrase'

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Your files have been decrypted.")

# List of files to decrypt (excluding specific files)
files = []

for file in os.listdir():
    if file not in ["voldemort.py", "thekey.key", "decrypt.py"]:
        if os.path.isfile(file):
            files.append(file)

print("Files to decrypt:", files)

# Decrypt the files
decrypt_files("thekey.key", files)
