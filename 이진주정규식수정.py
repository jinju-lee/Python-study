member=[0,0,0,0,0,0,0,0,0]

import re
r= re.compile('^[a-zA-Z]\w+')##ID 정규식
while True :
    str = input("ID입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[0]=str
         break   

import re
r= re.compile(r'^\d+\b')##Password 정규식
while True :
    str = input("Password입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[1]=str
         break
        
import re
r= re.compile(r'^[가-힣]+\b')##한글이름  정규식
while True :
    str = input("한글이름입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[2]=str
         break

import re
r= re.compile(r'^[a-zA-Z]+\b')##영문이름 정규식
while True :
    str = input("영문이름입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[3]=str
         break

import re
r= re.compile('\d{2,3}-\d{3,4}-\d{4}')##일반전화번호 정규식
while True :
    str = input("일반전화번호입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[4]=str
         break

import re
r= re.compile('\w+@\w+')##e-mail 정규식
while True :
    str = input("E-mail입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[5]=str
         break
        
import re
r= re.compile('\d{6}-\d{6}')##주민번호 정규식
while True :
    str = input("주민번호입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[6]=str
         break

import re
r= re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')##ip주소 정규식
while True :
    str = input("ip주소입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[7]=str
         break
        
import re
r= re.compile('^[^\s]\w+\.(txt|pdf|hwp|xls)')##자기소개서 파일 정규식
while True :
    str = input("자기소개서 파일입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         print(str)
         member[8]=str
         break

print(member)
    
        
        
