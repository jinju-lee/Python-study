import re

r=re.compile('[A-Z]')
e=re.compile('[A-Z]\w+\b')

print(r.search('Apple Banana Cherry'))
print(r.match('apple Banana Cherry'))
print(r.findall('Apple Banana Cherry'))

print(e.findall('aPple0 Banana Cher1ry'))
