inFp,outFp=None, None
inStr=""

inFp=open("c:/Windows/win.ini","r",encoding='ANSI')
outFp=open("c:/data3.txt","w",encoding='ANSI')

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('-----정상적으로 파일이 복사되었음-----')
