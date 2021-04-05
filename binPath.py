from datetime import timedelta, datetime
import sys
import os
from Crypto.Cipher import AES
import time
import binPathFull
#from Crypto.Util.Padding import pad, unpad

keys=list()


if (sys.version_info.major < 3):
    print("Script requires 3.x python version")
    sys.exit(-1)

#https://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii


def isAscii(bytes):
    for byte in bytes:
        if (byte< 0 or byte >127):
            return False
    return True        
    
 
#ct = cipher1.encrypt(pad(data, 16))
#pt = unpad(cipher2.decrypt(ct), 16)

    
def decrypt(min,max,cipherText, fOut):
    ivUsed=bytes([0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0x61,0x61])
    date = datetime.now()
    f = open("keys/"+fOut, "wt")
    if min == 0:
        min = 1
    iterator=0
    beginT  = datetime.now()        
    begin = time.time()
    while min != max:
        #beginSecs = time.time()
        keyBytes = min.to_bytes(32,'little')
        
        CipherObject = AES.new(keyBytes, AES.MODE_CBC, ivUsed)
        
        plainTextBytes = CipherObject.decrypt(cipherText)
        
     #   if min % (65536*25) == 0:
     #       print("\nMin "+hex(min)+" Max "+hex(max))
        if min % (65536*16) == 0:
            f.flush()
            iterator += 1
            #writeLog(min, max, begin, end)

        if (isAscii(plainTextBytes)):
            #end = time.time()
            #elapsed  = end-begin
            f.write("\n"+hex(min)+" "+str(iterator))
           
            
            
            #keys.append( (key, plainTextBytes.hex()) )
      #      writeLog(key,max,begin)
        min+=1
        
    
    end = datetime.now()
    elapsed = end - beginT
    print("\nFinished Combinations numbers checked  "+hex(min))
    print("Time elapsed for "+hex(min)+" (hh:mm:ss.ms) {}".format(elapsed))
    writeLog(min, max, elapsed)
    f.close()
            





def readLastLine(filename):
    print(filename)
    f = open(filename, "rt")
    allLines = f.readlines()
    f.close()
    retValue = int(allLines[-1], 16)
    return retValue

#if not os.path.exists("checkKeys"):
#    print("\n File to write log, doesnt exists()")
#else:
#    print("\n File to write log, exists()...deleting")
#    os.remove("checkKeys")
    
cipherText= binPathFull.readCipherText()

dir = os.listdir("keys")
mostRecentFile = max(dir)

nextIdx = int(mostRecentFile[8:], 16)
nextIdx+=1


mostRecentFile= "keyRange1"
newFile  = "keyRange"+str(nextIdx)
min = readLastLine("keys/"+mostRecentFile)
decrypt(min, 0xffffffff, cipherText,newFile)

