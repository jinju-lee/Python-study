html="""
<html>
    <head>
        <title> test web </title>
    </head>
    <body>
        <p align="center">text contents 1</p>
        <p align="right">text contents 2</p>
        <p align="left">text contents 3</p>
        <img src="c:\koala.jpg" width="500" height="300">
    </body>
</html>"""

from bs4 import BeautifulSoup
bs=BeautifulSoup(html)
            
import re

print(bs.find_all(text=re.compile('text +')))
tags=bs.find_all(re.compile("^p"))
tags
#print(bs.prettify())
#print(bs.find('title'))
#print(bs.find('p',align="center"))
#print(bs.find('p',align="right"))

#print(bs.find_all('head'))
#print(bs.find('html'))

body_tag=bs.fine('body')
list1=body_tag.find_all(['p','img']
for tag in list1:              
    print(tag)
