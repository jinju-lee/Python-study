import re
m=re.match('\s*\d+','   123')
print(m.group())
m=re.match('\s*(\d+)','    1234  ')
print(m.group(1))
