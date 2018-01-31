##전역변수##
money, c50000, c10000, c5000, c1000, c0 = 0, 0, 0, 0, 0, 0

##메인코드##
money=int(input("교환할 돈은 얼마? "))

c50000=money//50000
money %=50000
print("\n오만원짜리          ==> %s개" %c50000)

c10000=money//10000
money %=10000
print("만원짜리             ==> %s개" %c10000)

c5000=money//5000
money %=5000
print("오천원짜리         ==> %s개" %c5000)

c1000=money//1000
money %=1000
print("천원짜리             ==> %s개" %c1000)

c0=money
print("바꾸지 못한 잔돈 ==> %s개" %c0)

