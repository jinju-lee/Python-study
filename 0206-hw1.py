ch=int(input('진수(2/8/10/16)를 선택하시오\n'))
num1=input('첫 번째 수를 입력하시오.\n')
num2=input('두 번째 수를 입력하시오.\n')
if ch==2:
    num1='0b'+num1
    num2='0b'+num2
elif ch==8:
    num1='0o'+num1
    num2='0o'+num2
elif ch==16:
    num1='0x'+num1
    num2='0x'+num2
else:
    num1=num1
    num2=num2
    
num1_int=int(num1,ch)
num2_int=int(num2,ch)

print('두 수의 & 연산 결과\n')
print('16진수 => %s' %hex(num1_int&num2_int))
print('8진수 => %s' %oct(num1_int&num2_int))
print('10진수 => %s' %(num1_int&num2_int))
print('2진수 => %s\n' %bin(num1_int&num2_int))

print('두 수의 | 연산 결과\n')
print('16진수 => %s' %hex(num1_int|num2_int))
print('8진수 => %s' %oct(num1_int|num2_int))
print('10진수 => %s' %(num1_int|num2_int))
print('2진수 => %s\n' %bin(num1_int|num2_int))

print('두 수의 ^ 연산 결과\n')
print('16진수 => %s' %hex(num1_int^num2_int))
print('8진수 => %s' %oct(num1_int^num2_int))
print('10진수 => %s' %(num1_int^num2_int))
print('2진수 => %s\n' %bin(num1_int^num2_int))
