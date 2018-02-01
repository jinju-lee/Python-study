bank_num=input('계좌번호를 입력하시오: ')
    
if bank_num.isdigit()!=True:
    print('계좌번호: ', end='')
    
    for i in range(0,len(bank_num)):
        if bank_num[i]!='-':
            print(bank_num[i], end='')
        else:
            print('',end='')
else:
    print('계좌번호: %s' %bank_num)
            
