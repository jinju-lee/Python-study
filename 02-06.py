number=input('입력: ')
if number.isalpha()==True:
    print('글자입니다.')
elif number.isdigit()==True:
    print('숫자입니다.')
elif number.isalnum()==True:
    print('영숫자입니다.')
else:
    print('모르겠습니다.')
