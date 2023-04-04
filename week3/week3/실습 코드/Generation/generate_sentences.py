#단어 데이터베이스 사용을 위한 라이브러리
import nltk
import random

#로컬에 nltk에서 제공하는 words 데이터베이스를 다운받는다.
nltk.download('/Users/kangdonghee/nltk_data')
nltk.download('words')

# 100개의 문장 생성
num_sentences = 100
sentences = []

for i in range(num_sentences):
    # 7~10 단어를 무작위로 조합하여 문장 생성
    num_words = random.randint(7, 10)
    words = [random.choice(nltk.corpus.words.words()) for _ in range(num_words)]
    sentence = ' '.join(words)
    print(f'문장 생성 {i+1}/100 : {sentence}')
    sentences.append(sentence)

# 파일에 저장
with open('/Users/kangdonghee/Desktop/Computer Security/실습/week3/Generation/generated_sentences.txt', 'w') as file:
    file.write('\n'.join(sentences))
