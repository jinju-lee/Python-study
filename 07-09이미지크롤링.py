import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def bind_url():
    defaultURL='https://openapi.naver.com/v1/search/image.xml?'
    sort='sort=sim'
    start='&start=1'
    display='&display=10'
    query='&query='+urllib.parse.quote_plus(str(input('검색어를 입력하세요: ')))
    fullURL=defaultURL+sort+start+display+query
    #print(fullURL)
    return fullURL

def fetch_contents_from_url():
    url=bind_url()
    headers={
        'Host':'openapi.naver.com',
        'User_Agent':'curl/7.43.0',
        'Accept':'*/*',
        'Content-Type':'application/xml',
        'X-Naver-Client-Id':'DvzTcb3ar43hxGYljrMd',
        'X-Naver-Client-Secret':'fhSoSr4p7X'
        }
    r=urllib.request.Request(url,headers=headers)
    m=urllib.request.urlopen(r)
    html=m.read()
    return html

def extract_text_in_tags(tags, tagname="title"):
    txt=[]
    reg="[^<"+tagname+">][^<]+"
    print(reg)
    for tag in tags:
        txt.append(re.search(reg,tag).group())
    return txt

def get_contents_from_html():
    html=fetch_contents_from_url()
    title_tags=re.findall("<title>[^<]+</title>",html.decode('utf-8'))
    link_tags=re.findall("<link>[^<]+</link>",html.decode('utf-8'))
    titles=extract_text_in_tags(title_tags,tagname="title")
    links=extract_text_in_tags(link_tags,tagname='link')
    f=open("c:/image.html","w")
    f.write("<html><body>")
    for i in range(1,len(titles)):
        f.write("<p>"+titles[i]+"</p>")
        f.write("<img src="+links[i]+"/>")
    f.write("</body></html>")
    f.close()

get_contents_from_html()
