#!/usr/bin/python3
import sys
import os
import struct as s
normargs = sys.argv[1:]

def main(args):
    arch = args[0]
    files = args[1:]
    ar = open(arch,"wb")
    ar.write(bytes("POKEBALL","utf-8"))
    ar.write(bytearray([0]))
    for i in files:
        if os.path.isfile(i):
            if i!=arch:
                filesize = os.path.getsize(i)
                fname = bytes(i,"utf-8")
                data = s.pack(">128sq"+str(filesize)+"s",fname,filesize,open(i,"rb").read())
                print("PACKING %s..."%(i),end="\033[K\r")
                ar.write(data)
    print("")
    ar.close()

if len(normargs)>=2:
    main(normargs)
else:
    print("Usage: pokeball archive_name files")