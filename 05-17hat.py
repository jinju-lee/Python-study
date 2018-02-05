import re
r=re.compile('^c')
print(r.search('ckw'))
print(r.search('wck'))
print(r.search('sjs'))
