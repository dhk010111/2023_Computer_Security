import nltk
import time

nltk.download('words')
from nltk.corpus import words

word_list = set(words.words())

# 암호해독 함수
decrypt_time = []
def decrypt(text):
    start = time.time()
    candidates = []
    for key in range(1, 26):
        print(f'{key+1}/26 진행..')
        decrypted = ""
        for char in text:
            if char.isalpha():
                char_code = ord(char)
                char_code -= key
                if char.isupper():
                    if char_code < ord('A'):
                        char_code += 26
                    elif char_code > ord('Z'):
                        char_code -= 26
                else:
                    if char_code < ord('a'):
                        char_code += 26
                    elif char_code > ord('z'):
                        char_code -= 26
                decrypted += chr(char_code)
            else:
                decrypted += char
        # 후보군 리스트에 저장
        if any(word in word_list for word in decrypted.split()):
            candidates.append(decrypted)
    end = time.time()
    print(f'해독 진행 시간: {end - start}sec')
    decrypt_time.append(end-start)
    return candidates

# 해독 결과를 저장할 파일
output_file = open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Caesar/[Caesar]results.txt", "w")

# 암호문이 저장된 파일 불러오기
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Caesar/[Caesar]encrypted_sentences.txt", "r") as input_file:
    # 각각의 암호문 해독하기
    count = 0
    for line in input_file:
        print(f'{count + 1}/100 해독 진행..')
        encrypted = line.strip()
        # 모든 암호화 키 시도
        candidates = decrypt(encrypted)
        count += 1
        # 후보군 리스트에 저장된 문장들 중 일치하는 단어가 많은 문장 선택
        max_match = 0
        selected_candidate = ''
        for candidate in candidates:
            match_count = sum([word in word_list for word in candidate.split()])
            if match_count > max_match:
                max_match = match_count
                selected_candidate = candidate
        # words와 일치하는 단어가 많은 경우에만 파일에 입력
        if max_match > 0:
            output_file.write(selected_candidate + "\n")

output_file.close()

line_count = 0
total_time = 0
for i in decrypt_time:
    print(f'{line_count+1}번 라인 해독 시간 : {i:.4f}')
    line_count += 1
    total_time += i
print(f'평균 해독 시간 : {total_time/100:.4f} 초')
