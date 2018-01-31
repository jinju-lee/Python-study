price_pencil=3000
price_pen=4000

num_pencil=int(input('연필은 몇 개를 구입하시겠습니까?'))
num_pen=int(input('펜은 몇 개를 구입하시겠습니까?'))

total_price=(price_pencil*num_pencil)+(price_pen*num_pen)
Total=0.7*total_price
print('총 가격은 %s 원 입니다.' %Total)
