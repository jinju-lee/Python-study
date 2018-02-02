i,cnt,sum=0,0,0

for i in range(1,1001,2):
    sum+=i
    cnt+=1
    if sum>1000:
        print(i)
        break
    
