def func4(str7,str8,str9):

    member=[0,0,0,0,0,0,0,0,0]
    
    import re
    r= re.compile('\d{6}-\d{6}')##주민번호 정규식
    while True :
        if r.search(str7) == None:
             print("잘못입력")
             continue
        else :
             print(str7)
             member[6]=str7
             break

    import re
    r= re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')##ip주소 정규식
    while True :
        if r.search(str8) == None:
             print("잘못입력")
             continue
        else :
             print(str8)
             member[7]=str8
             break
            
    import re
    r= re.compile('^[^\s]\w+\.(txt|pdf|hwp|xls)')##자기소개서 파일 정규식
    while True :
        if r.search(str9) == None:
             print("잘못입력")
             continue
        else :
             print(str9)
             member[8]=str9
             break

    return (member[6],member[7],member[8])
