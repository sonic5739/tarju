# 신촌 날씨 출력하기
import urllib

from bs4 import BeautifulSoup as bs # html 언어 일어주는 함수 제공
import urllib.request as ur

# 신촌날씨 오도 출력하기

지역 = input("지역 : ")
검색어 = urllib.parse.quote( 지역 +'+날씨')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EC%8B%A0%EC%B4%8C%EB%82%98&qdt=0&ie=utf8&query=%EC%8B%A0%EC%B4%8C+%EB%82%A0%EC%94%A8'

앱문서 = ur.urlopen( url )
soup = bs( 앱문서.read() , 'html.parser')
온도 = soup.find_all( 'span' , {"class" : "todaytemp"} )
print( "현재 지역 날씨는 : " , 온도[0].text + "도 입니다 ")

# 신촌 날씨의 미세먼지 출력
미세먼지 = soup.find_all( 'dd' , {"class" : "lv1"})
print( "현재 신촌의 미세먼지 : " , 미세먼지[0].text)

# 신촌날씨의 오존지수 출력
오존지수 = soup.find_all("dd" , {"class" : "lv2"})
print("현재 신촌 오존지수 : " , 오존지수[0].text)