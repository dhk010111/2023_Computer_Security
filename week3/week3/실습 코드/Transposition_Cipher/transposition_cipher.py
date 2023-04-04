import math
import random
import string

def add_padding(text):
    #띄어쓰기를 포함할 경우 전치암호화하는 과정에서 줄바꿈이 발생하는 문제점 해결
    text = ''.join(text.split())
    text_len = len(text)
    # row, col 계산
    row = math.ceil(text_len**0.5)
    col = math.ceil(text_len/row)
    # padding에 추가할 문자 계산
    pad_len = row * col - text_len
    pad = ''.join(random.choices(string.ascii_lowercase, k=pad_len))
    # padding 추가
    padded_text = text + pad
    # 이차원 배열에 넣기
    matrix = [list(padded_text[i:i+col]) for i in range(0, row*col, col)]
    return matrix

def transposition_cipher(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # 열을 랜덤한 순서로 선택하기 위해 인덱스 리스트를 생성
    key = list(range(num_cols))
    random.shuffle(key)
    print(f'암호키(랜덤 생성) : {key}')
    # 랜덤한 순서로 열을 선택하여 1차원 리스트로 저장
    result = []
    for col_idx in key:
        for row_idx in range(num_rows):
            result.append(matrix[row_idx][col_idx])
    key = ''.join(str(k) for k in key)
    key_list.append(key)
    # 1차원 리스트를 문자열로 변환하여 반환
    return ''.join(result)

#평문을 불러와 암호화 진행
#---------------------------------
# generate_sentences.txt 파일에서 100개의 문장을 가져온다.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Generation/generated_sentences.txt", "r") as f:
    sentences = f.readlines()

count = 0
encrypted_sentences = []
key_list = []
for sentence in sentences:
    print(f'진행도 : {count+1}/100')
    matrix_text = add_padding(sentence)
    encrypted_sentence = transposition_cipher(matrix_text)
    encrypted_sentences.append(encrypted_sentence)
    count +=1
    print(f'암호화 이전 : {sentence}')
    print(f'암호화 결과 : {encrypted_sentence}')
    print()

# 암호화된 100개의 문장을 파일에 저장.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]encrypted_sentences.txt", "w") as f:
    f.write('\n'.join(encrypted_sentences))

with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]key.txt", "w") as f:
    f.write('\n'.join(key_list))