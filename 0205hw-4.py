height=int(input('키를 입력하세요: '))
weight=int(input('몸무게를 입력하세요: '))

BMI=weight/((height/100)*(height/100))

if BMI <20:
    print('BMI는 %6.2f로 저체중입니다.' %BMI)
elif BMI >=20 and BMI <=24:
    print('BMI는 %6.2f로 정상체중입니다.' %BMI)
elif BMI >=25 and BMI <=30:
    print('BMI는 %6.2f로 경도비만입니다.' %BMI)
else:
    print('BMI는 %6.2f로 비만입니다.' %BMI)
    
