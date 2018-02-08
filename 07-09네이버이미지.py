#크롤링을 위한 모듈 import
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def bind_url():
    #원하는 데이터를 요청하기 위한 url 생성(xml)
    defaultURL='https://openapi.naver.com/v1/search/image.xml?'
    #요청 변수 기본값으로 설정
    sort='sort=sim'
    start='&start=1'
    display='&display=10'
    #검색을 원하는 문자열을 입력받은 후 인코딩
    query='&query='+urllib.parse.quote_plus(str(input('검색어를 입력하세요: ')))
    #요청 url과 요청변수를 조합하여 fullURL 생성, 반환
    fullURL=defaultURL+sort+start+display+query
    #print(fullURL)
    return fullURL

def fetch_contents_from_url():
    #bind_url 함수에서 fullURL을 받아와 url변수에 저장
    url=bind_url()
    #헤더를 딕셔너리 형태로 생성
    headers={
        'Host':'openapi.naver.com',
        'User_Agent':'curl/7.43.0',
        'Accept':'*/*',
        'Content-Type':'application/xml',
        'X-Naver-Client-Id':'DvzTcb3ar43hxGYljrMd',
        'X-Naver-Client-Secret':'fhSoSr4p7X'
        }
    #조합된 최종 url에 데이터 요청
    r=urllib.request.Request(url,headers=headers)
    #최종 url open
    m=urllib.request.urlopen(r)
    #url에서 읽어 온 데이터를 html이라는 변수에 저장, 반환 
    html=m.read()
    return html

def extract_text_in_tags(tags, tagname):
    #빈 리스트 생성
    txt=[]
    #태그를 제외하고 텍스트만 남겨줌, 텍스트 반환
    reg="[^<"+tagname+">][^<]+"
    for tag in tags:
        txt.append(re.search(reg,tag).group())
    return txt

def get_contents_from_html():
    #fetch_contents_from_url함수로 html을 전달받아 html이라는 변수에 저장
    html=fetch_contents_from_url()
    #print(html)
    #태그를 제외하기 위해 정규식 사용, 디코딩
    title_tags=re.findall("<title>[^<]+</title>",html.decode('utf-8'))
    link_tags=re.findall("<link>[^<]+</link>",html.decode('utf-8'))
    #print(title_tags)
    #print(link_tags)
    #extract_text_in_tags함수로 title,link태그를 제외하고 저장한 txt를 받아옴 
    titles=extract_text_in_tags(title_tags,tagname="title")
    links=extract_text_in_tags(link_tags,tagname='link')
    #image.html 파일을 읽기모드로 생성하여 받아온 컨텐츠를 body태그에 넣어줌
    f=open("c:/image.html","w")
    f.write("<html><body>")
    for i in range(1,len(titles)):
        f.write("<p>"+titles[i]+"</p>")
        f.write("<img src="+links[i]+"/>")
    f.write("</body></html>")
    #파일닫음
    f.close()
    
#main문
get_contents_from_html()
