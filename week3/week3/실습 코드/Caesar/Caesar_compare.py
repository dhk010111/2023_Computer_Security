matching = 0


with open('/Users/kangdonghee/Desktop/Computer Security/실습/week3/Generation/generated_sentences.txt', 'r') as file1, \
    open('/Users/kangdonghee/Desktop/Computer Security/실습/week3/Caesar/[Caesar]results.txt', 'r') as file2:
    line = 0
    for line1, line2 in zip(file1, file2):
        if line1.strip() == line2.strip():
            print(f"{line+1}번 문장 Matching line: ", line1.strip())
            matching += 1
            line += 1
        else:
            print("Non-matching line: ")
            print("File1: ", line1.strip())
            print("File2: ", line2.strip())
            line += 1
    
    print(f'해독 성공률 : {matching/100*100}%')
        
