#동일한 폴더 안에 있는 함수 가져오기
import gen_pw, Brute_force

# 패스워드 10개씩 랜덤으로 생성하는 함수 실행
def run_generation():
    gen_pw.run()

#brute force 진행하는 함수
def run_brute_force(pw_length):
    print('Loading .. ')
    Brute_force.run(pw_length)


#문자열의 길이에 해당하는 txt를 가져와 brute force를 진행한다.
#run_brute_force(4)
#run_brute_force(5)
run_brute_force(6)
#run_brute_force(7)
#run_brute_force(8)
