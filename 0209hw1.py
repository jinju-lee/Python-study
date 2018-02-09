import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

kind=int(input('검색 분류를 입력하세요. 1-뉴스, 2-블로그, 3-카페'))
if kind==1:
    defaultURL='https://openapi.naver.com/v1/search/news.xml?'
elif kind==2:
    defaultURL='https://openapi.naver.com/v1/search/blog.xml?'
elif kind==3:
    defaultURL='https://openapi.naver.com/v1/search/cafearticle.xml?'
else:
    print('잘못 입력하셨습니다.')

key=str(input('검색어를 입력하세요: '))
name=str(input('파일명을 입력하세요: '))    
sort='sort=sim'
start='&start=1'
display='&display=100'
query='&query='+urllib.parse.quote_plus(key)
fullURL=defaultURL+sort+start+display+query
print(fullURL)
file=open("c:\\"+name,"w",encoding='utf-8')
headers={
    'Host':'openapi.naver.com',
    'User_Agent':'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id':'DvzTcb3ar43hxGYljrMd',
    'X-Naver-Client-Secret':'fhSoSr4p7X'
    }
req=urllib.request.Request(fullURL,headers=headers)
f=urllib.request.urlopen(req)
resultXML=f.read()
xmlsoup=BeautifulSoup(resultXML,'html.parser')

items=xmlsoup.find_all('item')

for item in items:
    file.write('------------------------------------------------\n')
    file.write('제목: ' + item.title.get_text(strip=True) + '\n')
    file.write('요약내용: ' + item.description.get_text(strip=True) + '\n')
    if kind==1:
        file.write('링크: '+item.originallink.get_text(strip=True)+'\n')
    elif kind==2:
        file.write('링크: '+item.bloggerlink.get_text(strip=True)+'\n')
    elif kind==3:
        file.write('링크: '+item.cafeurl.get_text(strip=True)+'\n')
    file.write('\n')
file.close()
