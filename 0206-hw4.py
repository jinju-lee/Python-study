import re

a=re.compile(r'[가-힣]*홍길동[가-힣]*\b')
b=re.compile(r'\w*홍길동\w*\b')
c=re.compile(r'\S*홍길동\S*\b')
str="""홍길동은 파이썬을 매우 잘하고 홍길동은 동에번쩍 서에번쩍하는홍길동은
만능인 홍길동의키는190이며 홍길동나이는&%$$##이다."""

print(a.findall(str))
print(b.findall(str))
print(c.findall(str))
