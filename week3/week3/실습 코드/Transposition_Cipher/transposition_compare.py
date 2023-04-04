matching = 0


with open('/Users/kangdonghee/Desktop/Computer Security/실습/week3/Generation/generated_sentences.txt', 'r') as file1, \
    open('/Users/kangdonghee/Desktop/Computer Security/실습/week3/Transposition_Cipher/[Trans]Decrypted_sentences.txt', 'r') as file2:
    line = 0
    for line1, line2 in zip(file1, file2):
        line1_stripped = line1.replace(" ", "").replace("\n", "")
        line2_stripped = line2.strip()
        if line1_stripped == line2_stripped:
            print(f"{line+1}번 문장 Matching line: ", line1.strip())
            matching += 1
            line += 1
        else:
            print("Non-matching line: ")
            print("File1: ", line1.strip())
            print("File2: ", line2.strip())
            line += 1
    
    print(f'해독 성공률 : {matching/100*100}%')
        
