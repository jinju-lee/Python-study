import re
r=re.compile(r'\w+\.html\b')
str="""aaa.html
bbb.html
ccc.xml
ddd.html
1.html
b.hhtml
hihihi.java
itpangpang.txt
ab123456a.js
Good.css
itit.html
ititkkk.htmlggg
hahahaha.htmlmlml
cabd_a.html
"""
print(r.findall(str))
