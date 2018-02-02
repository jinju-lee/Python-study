##함수 부분
def calc_monthly_salary(time, value):
    total=time*value
    print('총 급여: %s'%total)

##메인(main) 코드 부분
time=int(input('근무시간을 입력하세요: '))
value=int(input('시간당 급여를 입력하세요: '))
calc_monthly_salary(time, value)
    
