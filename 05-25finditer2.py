import re
p=re.compile('[a-zA-Z]+')

result=p.finditer('My birthday is October 23th.')

for i in result:
    print(i.group())
    print(i.span())
