from socket import *
HOST = ''                                     #(1)
# clinet 포트 번호
PORT = 11443                                  #(2)


s = socket(AF_INET, SOCK_STREAM)
# socket 일반 옵션 설정(일반, 주소 재사용)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)     #(3)
s.bind((HOST, PORT))
# 큐에 대기할 수 있는 횟수
s.listen(10)                                  #(4)

conn, addr = s.accept()
print ('Connected by', addr)
data = conn.recv(1024)
while 1:
     # command 입력받는 변수
     command = raw_input("Enter shell command or quit: ")   #(5)
     # 입력받은 command를 클라이언트로 전달
     conn.send(command)                                     #(6)
     if command == "quit": break 
     # 명령어 수행결과를 수신해서 출력
     data = conn.recv(1024)                                 #(7)
     print(data)
conn.close()
