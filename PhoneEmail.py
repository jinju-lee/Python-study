def func3(str5,str6):

    member=[0,0,0,0,0,0,0,0,0]
    
    import re
    r= re.compile('\d{2,3}-\d{3,4}-\d{4}')##일반전화번호 정규식
    while True :
        if r.search(str5) == None:
             print("잘못입력")
             continue
        else :
             print(str5)
             member[4]=str5
             break

    import re
    r= re.compile('\w+@\w+')##e-mail 정규식
    while True :
        if r.search(str6) == None:
             print("잘못입력")
             continue
        else :
             print(str6)
             member[5]=str6
             break

    return (member[4],member[5])
