import sys

##함수 정의 부분
def calc(v1, op, v2):
    result=0
    if op=='+':
        result=v1+v2
    elif op=='-':
        result=v1-v2
    elif op=='*':
        result=v1*v2
    elif op=='/':
        if v2==0:
            print('0으로 나눌 수 없습니다.')
            sys.exit(1)
        result=v1/v2
    elif op=='**':
        result=v1**v2
    return result

##변수 선언 부분
res=0
var1, var2,oper=0,0,...

##메인 코드 부분
oper=input('계산 입력 (+,-,*,/,**) : ')
var1=int(input('첫 번째 숫자 입력: '))
var2=int(input('두 번째 숫자 입력: '))
    
res=calc(var1, oper, var2)

    
print('##계산기 : %d %s %d = %d' %(var1,oper,var2,res))
