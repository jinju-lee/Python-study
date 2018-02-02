##함수 부분
def my_upper(lower):
    upper=lower-32
    print('변환 결과: %s'%chr(upper))

##메인(main) 코드 부분
low=ord(input('소문자를 입력하세요: '))
my_upper(low)
    
