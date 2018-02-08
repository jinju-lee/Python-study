#트위터 라이브러리 import
import tweepy

#트위터 application에서 발급받은 정보를 문자열로 입력 
Consumer_Key='vau477NqqBfo2iaK1YnEhFeP9'
Consumer_Secret='YGpaT4X8cBmedR2OuKKFM3ofbW9PjKq38uEh5NoF6MjlUJPQmo'
Access_Token='961421033352839170-IUbGM0u8lbgWkMPTM8b8q110fIihB7w'
Access_Token_Secret='9kvqUpSEGcDfcE88KIvdF1VDgLPyKjVHjetpoPo8yOuyM'

#핸들러 생성 및 개인정보 인증요청(api 인증 요청)
auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
#데이터 접근 요청(access 토큰 요청)
auth.set_access_token(Access_Token,Access_Token_Secret)
#twitter API 생성
api=tweepy.API(auth)

#검색할 키워드 입력
keyword='증권'

#결과 저장할 빈 리스트 생성
result=[]

#키워드로 검색한 결과를 리스트에 추가
#2페이지 반복
for i in range(1,3):
    tweets=api.search(keyword)
    for tweet in tweets:
        result.append(tweet)

#print(len(result))
#print(type(result[0])) #result의타입은 class'tweepy.models.Status'

'''
#리스트를 출력
for i in range(0,len(result)):
    print(result[i])
'''
'''
#리스트를 출력, 인코딩 에러가 날 경우 계속 진행
for i in range(0,len(result)):
    try:
        print(result[i])
    except UnicodeEncodeError:
        print('인코딩 에러입니다.')
        continue
'''
#텍스트 파일을 쓰기모드로 생성하여 리스트를 문자열로 변환해서 쓴다.
#인코딩 에러가 날 경우 계속 진행
f=open('c:/tweet.txt','w')
for i in range(0,len(result)):
    try:
        f.write(str(result[i])+'\n')
    except UnicodeEncoderError:
        print('인코딩 에러입니다.')
        continue
f.close()

