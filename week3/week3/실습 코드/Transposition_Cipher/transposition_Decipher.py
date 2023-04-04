import math

def decrypt_transposition_cipher(ciphertext, key, count):
    key = [int(char) for char in key]
    num_rows = math.ceil(len(ciphertext)/len(key))
    num_cols = len(key)
    print(f'해독 진행 : {count+1}/100')
    print(f'적용 키 값 : {key}')
    # 인덱스 리스트를 생성하여 역순으로 정렬
    try:
        key_inv = [key.index(i) for i in range(num_cols)]
    except ValueError:
        return None
    # 1차원 리스트를 이차원 배열에 복원
    matrix = [list(ciphertext[i:i+num_cols]) for i in range(0, num_rows*num_cols, num_cols)]
    # 복호화된 결과를 저장할 리스트
    result = []
    # 역순으로 정렬된 인덱스를 사용하여 원래의 순서로 문자열을 복원
    for col_idx in key_inv:
        for row_idx in range(num_rows):
            result.append(matrix[row_idx][col_idx])
    # 복호화된 결과를 문자열로 변환하여 반환
    final = ''.join(result)
    print(f'해독 결과 : {final}')
    return final

# 암호화된 문장을 불러온다.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]encrypted_sentences.txt", "r") as f:
    encrypted_sentences = f.readlines()

# 암호화된 문장을 복호화
# 저장된 키 값을 불러와 리스트로 변환
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]key.txt", "r") as f:
    key_str = f.read()
key_list = key_str.split()
key_num = 0
decrypted_sentences = []
count = 0
for encrypted_sentence in encrypted_sentences:
    decrypted_sentence = decrypt_transposition_cipher(encrypted_sentence.strip(), key_list[key_num], count)
    if decrypted_sentence:
        decrypted_sentences.append(decrypted_sentence)
    key_num += 1
    count += 1

# 복호화된 문장을 파일에 저장한다.
with open("/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]decrypted_sentences.txt", "w") as f:
    f.write('\n'.join(decrypted_sentences))
