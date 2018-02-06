from IdPassword import *
from Name import *
from PhoneEmail import *
from PnIpFile import *

##변수 선언 부분
member=[0,0,0,0,0,0,0,0,0]

##메인(main) 코드 부분
str = input("ID입력")
str2 = input("Password입력")
(member[0],member[1])=func1(str,str2)
        
str3 = input("한글이름입력")
str4 = input("영문이름입력")
(member[2],member[3])=func2(str3,str4)


str5 = input("일반전화번호입력")
str6 = input("E-mail입력")
(member[4],member[5])=func3(str5,str6)

str7 = input("주민번호입력")
str8 = input("ip주소입력")
str9 = input("자기소개서 파일입력")
(member[6],member[7],member[8])=func4(str7,str8,str9)

print(member)
    
        
        
