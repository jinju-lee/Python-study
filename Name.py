def func2(str3,str4):

    member=[0,0,0,0,0,0,0,0,0]
    
    import re
    r= re.compile(r'^[가-힣]+\b')##한글이름  정규식
    while True :
        if r.search(str3) == None:
             print("잘못입력")
             continue
        else :
             print(str3)
             member[2]=str3
             break

    import re
    r= re.compile(r'^[a-zA-Z]+\b')##영문이름 정규식
    while True :
        if r.search(str4) == None:
             print("잘못입력")
             continue
        else :
             print(str4)
             member[3]=str4
             break

    return (member[2],member[3])
