import re

r=re.compile('https?://.+\? (.+)')
c=re.compile('\? (.+)')
a=re.compile('https?://(.+)\? .+')
b=re.compile('https?://[^?]+')
str="""https://www.daum.net/abc/top? a=b&c=d"""
str2="""https://a.b.c/abc/bbb/ccc? a=b&c=d"""

print(r.findall(str))
print(c.findall(str))
print(a.findall(str))
print(b.findall(str2))
