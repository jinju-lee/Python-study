while True:
    n=0
    number=int(input('Enter the number: '))
    if number ==0:
        print('종료합니다')
        break

    for i in range(2,number+1):
        if number%i==0 and number!=i:
            n+=1
            
    if n>0 or number==1:
        print('%s 은 소수가 아닙니다.'%number)
    elif n==0 :
        print('%s 은 소수입니다.'%number)
