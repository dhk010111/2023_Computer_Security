import random

def caesar_cipher(text, key):
    #반환할 암호문 선언
    shifted_text = ""
    for char in text:
        if char.isalpha():
            #시저암호의 수식 이용하여 암호화 진행
            if char.isupper(): #아스키코드값을 이용해 대문자일 경우 shift 진행
                shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else: #소문자에 대해서도 shift 진행
                shifted_char = chr((ord(char) - 97 + key) % 26 + 97)
        else:
            shifted_char = char
        shifted_text += shifted_char
    print(f'평문 : {text}')
    print(f'암호화 Key(shift) : {key}')
    print(f'암호화 : {shifted_text}')
    return shifted_text

# generate_sentences.txt 파일에서 100개의 문장을 가져온다.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Generation/generated_sentences.txt", "r") as f:
    sentences = f.readlines()

# 각 문장을 caesar_cipher(text,key)를 적용하여 암호화.
encrypted_sentences = []
count = 0

for sentence in sentences:
    # 1에서 25 사이의 랜덤한 정수로 key 값을 생성한다. (각 문장마다 랜덤한 키값으로 암호화 진행)
    key = random.randint(1, 25)
    encrypted_sentence = caesar_cipher(sentence.strip(), key)
    encrypted_sentences.append(encrypted_sentence)
    count +=1
    print(f'진행도 : {count}/100')
    print()


# 암호화된 100개의 문장을 파일에 저장.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Caesar/[Caesar]encrypted_sentences.txt", "w") as f:
    for sentence in encrypted_sentences:
        f.write(sentence + "\n")