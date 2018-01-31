##전역변수##
money, c500, c100, c50, c10, c0 = 0, 0, 0, 0, 0, 0

##메인코드##
money=int(input("교환할 돈은 얼마? "))

c500=money//500
money %=500
print("\n오백원짜리          ==> %s개" %c500)

c100=money//100
money %=100
print("백원짜리             ==> %s개" %c100)

c50=money//50
money %=50
print("백원짜리             ==> %s개" %c50)

c10=money//10
money %=10
print("십원짜리             ==> %s개" %c10)

c0=money
print("바꾸지 못한 잔돈 ==> %s개" %c0)

