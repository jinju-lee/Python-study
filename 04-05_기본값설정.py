def cal(num1=0, num2=1,method='sum'):
    if method=='sum':
        print(num1+num2)
    elif method=='min':
        print(num1-num2)
    elif method=='prod':
        print(num1*num2)

cal(1,2)
cal(1,2,'prod')
cal(1,2,'min')
cal()
