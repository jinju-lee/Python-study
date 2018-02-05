import re
r=re.compile('ab?c')
print(r.search('abc'))
print(r.search('ac'))
print(r.search('abc').group())
print(r.search('ac').group())
print(r.search('abbc').group())
