hour=int(input('시각을 입력하시오: '))
minute=int(input('분을 입력하시오: '))
sec=int(input('초를 입력하시오: '))
total_sec=(hour*60*60)+(minute*60)+(sec)
print('전체 초는 %s 초 입니다.' %total_sec)
