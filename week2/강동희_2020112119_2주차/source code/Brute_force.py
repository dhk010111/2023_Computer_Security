import time
import itertools
import string


# 가능한 문자들의 리스트 (숫자, 알파벳, 특수문자)
pw_list = string.digits+string.ascii_letters+string.punctuation

# 모든 경우의 수를 생성하여 pw_list와 매칭
def brute_force(answer_list):
    count = 0
    timer = []
    #패스워드 매칭까지 걸린 시간 측정
    start = time.process_time()
    for pw_len in range(4, 8):
        #
        for password in itertools.product(pw_list, repeat=pw_len):
                # brute force로 맞출 문자열 생성
                password = "".join(password)
                # 생성된 패스워드가 매칭될 경우
                if password in answer_list:
                    #매칭된 시간 측정
                    end = time.process_time()
                    #찾은 비밀번호 출력
                    print(f"비밀번호 {password} 찾았습니다.")
                    #걸린 시간 및 남은 패스워드 개수 출력
                    print(f'{end-start} 진행도 : {count+1}/{len(answer_list)}')
                    timer.append(end-start)
                    print("Loading .. ")
                    count += 1
                #모든 리스트와 매칭될 경우 종료
                if count == len(answer_list):
                    print(timer)
                    exit()    
    

def import_test_pw(length):
    #정답 리스트를 가져온다
    test_pw_file = f'/Users/kangdonghee/Desktop/Computer Security/실습/week2/PW{length}.txt'
    with open(test_pw_file) as f:
        test_pw = f.readlines()
    #라인 하나씩 가져와 리스트에 저장
    test_pw = [line.rstrip('\n') for line in test_pw]
    return test_pw

#패스워드 탐색 시작 함수
def run(pw_length):
    test_pw = import_test_pw(pw_length)
    brute_force(test_pw)
    return print('Done.')
