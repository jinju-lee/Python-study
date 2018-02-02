i, hap=0,0
num1, num2,num3=0,0,0

num1=int(input('시작값 입력: '))
num2=int(input('끝값 입력: '))
num3=int(input('증가값 입력: '))

i=num1
hap=num1

while i<num2:
    hap+=(i+num3)
    i+=num3

print('%d에서 %d까지 %d씩 증가한 값의 합: %d' %(num1, num2, num3, hap))
 
