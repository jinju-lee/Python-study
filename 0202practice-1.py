i=0

num1=int(input('첫번째 숫자를 입력하세요: '))
num2=int(input('두번째 숫자를 입력하세요: '))

if num1<0 and num2<0:
    print('두 수의 곱은 양수입니다.')
elif num1>0 and num2>0:
    print('두 수의 곱은 양수입니다.')
elif num1>0 and num2<0:
    print('두 수의 곱은 음수입니다.')
elif num1<0 and num2>0:
    print('두 수의 곱은 음수입니다.')
