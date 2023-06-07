# -*- coding: utf-8 -*-

import sys
import os
import hashlib
import zlib
from io import StringIO

VirusDB = [] #악성코드 패턴은 모두 virus.db에 존재함
vdb = [] #가공된 악성코드 DB가 저장된다.
vsize = [] #악성코드의 파일 크기만 저장한다.

def DecodeKMD(fname):
    try:
        fp = open(fname, 'rb')
        buf = fp.read()
        fp.close()

        buf2 = buf[:-32]
        fmd5 = buf[-32:]

        f = buf2
        for i in range(3) :
            md5 = hashlib.md5()
            md5.update(f)
            f = md5.hexdigest()

        if f != md5:
            raise SystemError
        
        buf3 = ''
        for c in buf2[4:] :
            buf3 += chr(ord(c) ^ 0xFF)

        buf4 = zlib.decompress(buf3)
        return buf4
    except:
        pass
    return None

# virus.db 파일에서 악성코드 패턴을 읽는다.
def LoadVirusDB():
    buf = DecodeKMD('virus.kmd')
    fp = StringIO(buf)

    while True:
        line = fp.readline()
        if not line : break
        
        line = line.strip()
        line = line.decode('utf-8')
        VirusDB.append(line)

    fp.close()

def MakeVirusDB():
    for pattern in VirusDB:
        t = []
        v = pattern.split(':')
        t.append(v[1])
        t.append(v[2])
        vdb.append(t)

        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)

def SearchVDB(fmd5):
    for t in vdb:
        if t[0] == fmd5:
            return True, t[1]
    return False, ''

if __name__ == '__main__':
    LoadVirusDB()
    MakeVirusDB()

    if len(sys.argv) != 2:
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

        ret, vname = SearchVDB(fmd5)
        if ret == True:
            print('%s : %s' %(fname, vname))
            os.remove(fname)
        else:
            print('%s : ok' %(fname))
    else:
        print('%s : ok' %(fname))
