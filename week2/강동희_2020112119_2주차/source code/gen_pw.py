import string
import random

#string 모듈을 통해 숫자, 알파벳(대&소), 특수문자를 리스트로 생성
list1 = string.digits
list2 = string.ascii_letters
list3 = string.punctuation


#패스워드 길이마다 유형별로 조합하여 랜덤으로 패스워드를 생성하는 함수
def pw_type(type, length):
    passwords = []
    if type == 0: #숫자 조합
        for _ in range(10): #10개씩 생성하기 위함
            password = ''.join(random.sample(list1, length)) #랜덤 조합을 통해 패스워드 길이의 문자열 생성
            passwords.append(password) #생성된 문자열을 리스트에 저장

    if type == 1: #알파벳 조합
        for _ in range(10): #10개씩 생성하기 위함
            password = ''.join(random.sample(list2, length)) #랜덤 조합을 통해 패스워드 길이의 문자열 생성
            passwords.append(password) #생성된 문자열을 리스트에 저장

    if type == 2: #특수문자 조합
        for _ in range(10): #10개씩 생성하기 위함
            password = ''.join(random.sample(list3, length)) #랜덤 조합을 통해 패스워드 길이의 문자열 생성
            passwords.append(password) #생성된 문자열을 리스트에 저장

    if type == 3: #숫자+알파벳 조합
        count = 0
        while(count <= 9): #10개씩 생성하기 위함
            password = "".join(random.choice(list1 + list2) for _ in range(length)) #조합된 유형(숫자+알파벳)으로 랜덤 생성
            if all(any(word in password for word in lst) for lst in (list1, list2)): #그 중 모든 리스트에서 적어도 문자 1개 이상 포함된 문자열을 선택하여
                passwords.append(password) #리스트에 저장
                count += 1

    if type == 4: #숫자+특수문자 조합
        count = 0
        while(count <= 9): #10개씩 생성하기 위함
            password = "".join(random.choice(list1 + list3) for _ in range(length)) #유형 3과 동일
            if all(any(word in password for word in lst) for lst in (list1, list3)):
                passwords.append(password)
                count += 1
                
    if type == 5: #알파벳+특수문자 조합
        count = 0
        while(count <= 9): #10개씩 생성하기 위함
            password = "".join(random.choice(list2 + list3) for _ in range(length)) #유형 3과 동일
            if all(any(word in password for word in lst) for lst in (list2, list3)):
                passwords.append(password)
                count += 1

    if type == 6: #숫자+알파벳+특수문자 조합
        count = 0 
        while(count <= 9): #10개씩 생성하기 위함
            password = "".join(random.choice(list1 + list2 + list3) for _ in range(length)) #유형 3과 동일
            if all(any(word in password for word in lst) for lst in (list1, list2, list3)):
                passwords.append(password)
                count += 1
    return passwords

def run():
    for length in range(4, 9): #4자리~8자리의 패스워드를 생성한다.
        file = f'/Users/kangdonghee/Desktop/Computer Security/실습/week2/PW{length}.txt' #미리 생성한 자릿수별로 구분된 파일을 불러온다.
        with open(file, "w+") as pw_file: #파일을 열어 write 한다.
            for type in range(0, 7): #모든 유형별로 생성
                pw_file.write('\n'.join(pw_type(type, length))) #생성된 패스워드를 파일에 작성한다.
                pw_file.write('\n')
        pw_file.close() #파일 닫기
        passwords = [] #길이 패스워드에 대해 초기화
    return print('Generation Done.') #생성 종료 문구 출력
