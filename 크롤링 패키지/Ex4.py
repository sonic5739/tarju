# 자동차 모델명 입력을 받아 출시가 크
from bs4 import BeautifulSoup as bs # html 언어 일어주는 함수 제공
import urllib.request as ur
import urllib
while True :
    모델명 = input("모델명 : ")
    검색어 = urllib.parse.quote(모델명)
    주소 = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + 검색어

    앱문서 = ur.urlopen( 주소 )
    s0up = bs( 앱문서.read() , 'html.parser')
    가격 = s0up.find_all("span" , {"class" : ""})
    찾는문자 = "판매"

    for i in 가격 :
        b = 찾는문자 in i.text # 만약에 가격에 판매가 포함되어 있으면
        if b :
            print( "현재 모델의 출시가 : " + i.text)