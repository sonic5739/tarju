# 검색결과는
# 발급받은 애플리케이션 정보를 변수에 저장
import json
import re

ClientID = 'O7Pg94YPM2lKlLGRptPP'
ClientSecret = 'ykyhwzVaiS'

# documents 파이썬 코드를 복사 해우기
import os
import sys
import urllib.request
client_id = ClientID
client_secret = ClientSecret

# 직접입력해서 검색하기
검색어 = input(" 블로그 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# 책 검색
검색어 = input(" 책 검색 : ")
encText = urllib.parse.quote(검색어)
urlrl = "https://openapi.naver.com/v1/search/book.json?query=" + encText


urequest = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8') # 한글 지원

    json결과 = json.loads(검색결과)

    for i in json결과['items'] :
        타이틀 = re.sub('<.+?>', '',i['title'], 0 , re.I | re.S )
        print(타이틀)

else:
    print("Error Code:" + rescode)
# 뉴스 검색
검색어 = input(" 뉴스 검색 : ")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/news?query=" + encText

urequest = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)