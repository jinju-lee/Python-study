per_num=input('주민등록번호 입력: ')
if (per_num[7]=='1') | (per_num[7]=='3'):
    print('남자입니다.')

elif (per_num[7]=='2') | (per_num[7]=='4'):
    print('여자입니다.')

else:
    print('잘못 입력하셨습니다.')
