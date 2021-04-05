So, this is a python program, that uses PoC to break ciphers, what it does is that uses a key, and keeps incrementing one to the key, and decrypting (its a burte force approach). For 1 int , i got 5 days...so for 8 int i would get 5*8 days...which is not bad, i guess...actually my computer is quite slow :)..I need programmers to code this in c and asm, or whatever language faster. I tried to use java ,but i think it was slow, anyway i have two git repos binPath and binPathShort, binPathShort is a subset of binPath , since this project escalated.
This checks the plaintext for ascii characters, so its a known plaintext attack
it also assumes that you know the IV, and the salt...
also the keys/ dir has keyRange tested.

0xhexanumber (key tried) , iteration (each iteration is like 65536*16, but it can change programatically). Iteratations are to estimate the time to decrypt.
so for example,

format of keyRange:

0xffaf12ab 123
0xffaf12ad 123

files/ has files to encrypt and decrypt

Also not sure if this runs on python2 ..it has a check on the code, but you can change it to version 2 on the code.

Later :)
