try:
    no1=6
    no2=0
    no1/no2
except (ZeroDivisionError,ValueError):
    print('에러가 발생했습니다.')
