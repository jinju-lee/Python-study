##변수 선언 부분
number,i,cnt=0,0,0

##함수 부분
def print_readable_bin(number):
    number_bin=bin(number)
    for i in range(0, len(number_bin)):
        print(number_bin[i],end='')
        for cnt in range(0,len(number_bin)//4):
            if i==(3*(cnt+1))+cnt:
                print('_',end='')

##메인(main) 코드 부분
num=int(input('숫자를 입력하세요: '))
print_readable_bin(num)
