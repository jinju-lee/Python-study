import re
#r=re.compile('ab{2}c')
#print(r.search('abbc'))
#print(r.search('ac').group())
m=re.compile('ab{2,5}c')
print(m.search('abbc'))
print(m.search('abbbbc').group())
