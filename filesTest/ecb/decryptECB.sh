#!/bin/bash
#-salt, -nosalt, -S salt
#These options allow to switch salting on or off. With -S salt it is possible to explicitly give its value (in hexadecimal
# -p , prints iv, salt and key
# -nopad , dont add pad
openssl enc -d -p -aes-256-ecb -nosalt -K 6161 -in cipherText -out plainTextDecrypted16
