data=[ ]
n=0

while True:
    import re
    r=re.compile(r'^[가-힣]{1,5}\b')##이름
    while True :
        str = input("이름: ")

       
        if r.search(str) == None:
            if str=='q':
                break
            else:
                print("잘못입력")
                continue
        else :
             print(str)
             data.append(str)
             break
    if str=='q':
        break
    import re
    r= re.compile('(199|200|201)[0-9]')##학번
    while True :
        str = input("학번: ")
        if r.search(str) == None:
             print("잘못입력")
             continue
        else :
             print(str)
             data.append(str)
             break
            
    import re
    r= re.compile('^(서울|대전|대구|부산|광주|인천|울산|경북|경남|충북|충남|제주|강원|전북|전남)+\S{1,20}')##주소
    while True :
        str = input("주소: ")
        if r.search(str) == None:
             print("잘못입력")
             continue
        else :
             print(str)
             data.append(str)
             break

    import re
    r= re.compile(r'^\d{6}\b')##생년월일
    while True :
        str = input("생년월일: ")
        if r.search(str) == None:
             print("잘못입력")
             continue
        else :
             print(str)
             data.append(str)
             n+=1
             break

f=open("c:\\hw1.txt","w")
for i in range(0,len(data)):
    if i==0:
        d=data[i]+','
    else:
        if i==len(data)-1:
            d+=data[i]
            break
        d+=data[i]+','
f.write(d)
f.close()
f=open("c:\\hw1.txt","r")
informs=f.readlines()
for i in informs:
    print(i)
