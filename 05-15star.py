import re
r=re.compile('ab*c')
print(r.search('abbdc'))
print(r.search('ac').group())
print(r.search('abbdc').group())
