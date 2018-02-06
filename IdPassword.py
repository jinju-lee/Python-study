def func1(str,str2):
    
    member=[0,0,0,0,0,0,0,0,0]
    
    import re
    r=re.compile('^[a-zA-Z]\w+')##ID 정규식
    while True:
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

        if r.search(str2) == None:
             print("잘못입력")
             continue
        else :
             print(str2)
             member[1]=str2
             break

    return (member[0],member[1])
