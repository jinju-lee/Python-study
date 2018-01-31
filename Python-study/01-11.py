sec=0
minute=0
time=0

time=int(input("초 단위의 시간을 입력하세요: "))

minute=time//60
sec=time%60

print("%s 초는 %s 분 %s 초 입니다." %(time, minute, sec))
