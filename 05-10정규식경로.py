import re
url='<a href="C:\Python34\Koala.jpg">그림</a><font size="10">'
print(re.search('href="(.*?)"',url).group(1))
