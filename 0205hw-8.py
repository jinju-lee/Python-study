n=0

height=float(input('높이를 입력하세요(m):'))

while height>0.00001:
    height= height/2
    n+=1
    
print('공이 튀긴 횟수는 %s 회 입니다.' %n)
