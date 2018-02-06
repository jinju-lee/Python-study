import re
a=re.compile('전화번호: (\d{3}-\d{3,4}-\d{4})')
b=re.compile('날짜: \d{2}.+ \d{1,2}.+ \d{1,2}.+')
c=re.compile('.+홍길동.+')

str="""
A: 홍길동은 살아있다.
B: 아냐, 그는 죽었어.

전화번호: 010-1111-1111
전화번호: 010-2233-4444
전화번호: 010-7777-5555

날짜: 95년 1월 1일
"""

print(a.findall(str))
print(b.findall(str))
print(c.findall(str))
