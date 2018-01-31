a=100
result=0
i=0
num=0
n=0

num=int(input("시프트할 숫자는?"))
n=int(input("출력할 횟수는?"))

for i in range(1,n+1) :
    result=num<<i
    print("%d << %d=%d" %(num, i, result))

for i in range(1,n+1) :
    result=num>>i
    print("%d >> %d=%d" %(num, i, result))


