def calculator(num1_int,num2_int):
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

