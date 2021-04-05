#!/bin/bash
#-salt, -nosalt, -S salt
#These options allow to switch salting on or off. With -S salt it is possible to explicitly give its value (in hexadecimal
# -P , prints iv, salt and key
# -e encrypts (default) -d decrpyts
# -a base26
openssl enc -aes-256-ecb -nosalt -p -K 6161 -in plainText16 -out cipherText

