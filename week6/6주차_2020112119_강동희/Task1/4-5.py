# -*- coding: utf-8 -*-
import hashlib
import os

#text 파일 바이너리 읽기 모드(rb)로 오픈
fp=open('/Users/kangdonghee/Desktop/week6/Task1/eicar_edit.txt', 'rb')
fbuf=fp.read()
fp.close()


m=hashlib.md5()
#md5 해쉬 구하기
m.update(fbuf)
#file의 md5값을 저장
fmd5=m.hexdigest()

#파일의 md5 해시 값이 eicar 바이러스 해시값과 일치할 경우
if fmd5 == "44d88612fea8a8f36de82e1278abb02f":
    #Virus 출력 및 파일 삭제
    print("Virus")
    os.remove('eicar.txt')
else:
    #아닐 경우 No Virus 출력
    print("No Viurs")
