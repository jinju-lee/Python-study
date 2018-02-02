##변수 선언 부분
select, answer, numStr, num1, num2=0, 0, ...,0,0

##함수 부분
def calculator(number):
    answer=eval(number)
    print('%s 결과는 %5.1f 입니다. ' %(number, answer))
def plus(number1, number2):
     answer=0
     for i in range(number1, number2+1):
            answer=answer+i
     print('%d+ ...+%d는 %d 입니다.'%(number1, number2, answer))

##메인(main) 코드 부분
while True:
    select=int(input('1.수식 계산기  2.두 수 사이 합계 : '))

    if select==1:
        numStr=input('***수식을 입력하세요: ')
        calculator(numStr)
    elif select==2:
        num1=int(input('***첫번째 숫자를 입력하세요: '))
        num2=int(input('***두번째 숫자를 입력하세요: '))
        plus(num1, num2)
    elif select==0:
        break
    else:
        print('1 또는 2만 입력해야 합니다.')

