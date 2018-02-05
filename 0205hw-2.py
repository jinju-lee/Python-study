cnt=0

store={'사과':1000, '포도':3000, '배':2000, '귤':500}
number={'사과':0, '포도':0, '배':0, '귤':0}

while True:
    a=input('구입하려는 과일의 이름을 입력하세요. (입력을 종료하려면 q를 입력)')
    if a=='q':
        break
    b=int(input('구입하려는 과일의 개수를 입력하세요.'))
    number[a]+=b #누적
    
    apple_price=number['사과']*store['사과']
    if number['포도']>=3:
        grape_price=number['포도']*store['포도']*0.9
    else:
        grape_price=number['포도']*store['포도']
    pear_price=number['배']*store['배']
    tangerine_price=number['귤']*store['귤']

    if number['귤']//10 !=0:
        number['귤']+=(number['귤']//10)*2

total=apple_price+grape_price+pear_price+tangerine_price
print('귀하는', end= ' ')
if number['사과']>0:
    print('사과 -> %s 개 :  금액 %s 원' %(number['사과'], apple_price), end=' ')
if number['포도']>0:
    print('포도 -> %s 개 :  금액 %s 원' %(number['포도'], grape_price), end=' ')
if number['배']>0:
    print('배 -> %s 개 :  금액 %s 원' %(number['배'], pear_price), end=' ')
if number['귤']>0:
    print('귤 -> %s 개 :  금액 %s 원' %(number['귤'], tangerine_price), end=' ')
print('총 금액 %s를 구입했습니다.' %total)
