import re
r=re.compile('python')

m=r.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())

r=r.search('python')
print(r.group())
print(r.start())
print(r.end())
print(r.span())
