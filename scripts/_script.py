# this is the simple script for getting the all directory expect the main file from the systems & it works on both linux & windows.
import os

files = []

for file in os.listdir():
    if file == "_sript.py":
        continue
    files.append(file)
print(files)