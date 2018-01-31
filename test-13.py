x1=int(input('첫 번째 x좌표를 입력하세요: '))
y1=int(input('첫 번째 y좌표를 입력하세요: '))
x2=int(input('두 번째 x좌표를 입력하세요: '))
y2=int(input('두 번째 y좌표를 입력하세요: '))

area=(x2-x1)*(y2-y1)/2
if area<0:
    area=-area
    
print('직각삼각형의 넓이는 %s 입니다' %area)
