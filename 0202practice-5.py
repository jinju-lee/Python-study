fruits=input('과입을 입력하세요. (,구분) : ')

fruits_split=fruits.split(',')

for i in range(len(fruits_split)-1,-1,-1):
    if i==0:
        print(fruits_split[i],end=' ')
        break
    print(fruits_split[i],end=',  ')
    
