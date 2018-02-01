num=0
num5=0
num4=0
num3=0
num2=0
num1=0
total=0

num=int(input("정수를  입력하세요: "))

num5=num//10000
num4=(num%10000)//1000
num3=(num%1000)//100
num2=(num%100)//10
num1=(num%10)//1
total=num5+num4+num3+num2+num1

print(num5)
print(num4)
print(num3)
print(num2)
print(num1)
print("%s 의 모든 자리수의 합은 %s 입니다." %(num, total))
