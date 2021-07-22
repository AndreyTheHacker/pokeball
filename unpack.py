#!/usr/bin/python3
import struct as s
import sys
import time

if len(sys.argv[1:])!=1:
    print("Usage: %s archive"%(sys.argv[0]))

data = open(sys.argv[-1],"rb")
if(data.read(8)!=b'POKEBALL'):
    print("This file is not a Pokeball archive...")
    exit()
data.seek(9)
z = 9

swk = ["|","/","-","\\"]
swb = [0,len(swk)-1]
def print_unpack(name):
    print("UNPACKING %s... %s"%(name,swk[swb[0]]),end='\033[K\r')
    if swb[0]==swb[1]: swb[0]=0
    swb[0]+=1

def normalize(btr):
    return ''.join([s if s!="\x00" else "" for s in btr])

while True:
    data.seek(z)
    mn = s.calcsize(">128sq")
    try:
        pk = s.unpack(">128sq",data.read(mn))
        pos = z+mn
        name = normalize(pk[0].decode("utf-8"))
        print_unpack(name)
        data.seek(pos)
        fdata = data.read(pk[-1])
        wrt = open(name,"wb")
        wrt.write(fdata)
        wrt.close()
        z+=pk[-1]+mn
    except s.error as e:
        print("")
        print("Unpacked succesfully!")
        break