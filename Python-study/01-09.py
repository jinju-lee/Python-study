time=0
pay=0
total=0

time=int(input("근로시간을 입력하세요: "))
pay=int(input("시간당 임금을 입력하세요: "))

total=time*pay
print("당신의 급여는 %s 원 입니다" %total)
