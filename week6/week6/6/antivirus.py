# -*- coding: utf-8 -*-

import sys
import hashlib
import os

VirusDB = []
vdb = []
vsize = []

def LoadVirusDB() :
    fp = open('virus.db', 'rb')

    while True:
        line = fp.readline()
        print(line)
        if not line : break

        line = line.strip()
        VirusDB.append(line)

def MakeVirusDB():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[0])
        t.append(v[1])
        vdb.append(t)

        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)

def SearchVDB(fmd5):
    for t in vdb:
        if t[0] == fmd5 :
            return True, t[1]
        
    return False, ''

if __name__ == '__main__':
    MakeVirusDB()

    if len(sys.argv) !=2:
        print('Usage : antivirus.py [file]')
        exit(0)

    fname = sys.argv[1]

    size = os.path.getsize(fname)
    if vsize.count(size):
        fp = open(fname, 'rb')
        buf = fp.read()
        fp.close()

        m = hashlib.md5()
        m.update(buf)
        fmd5 = m.hexdigest()
        print(fmd5)
        ret, vname = SearchVDB(fmd5)
        if ret == True:
            print('%s : %s' %(fname, fname))
            os.remove(fname)
        else:
            print('%s : ok' %(fname))
    else :
        print('%s : ok' %(fname))