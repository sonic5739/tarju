# 정보수집_크롤링 패키지
    # 1. Ex1.py

# 크롤링 : 인터넷에서 데이터 추출하기
    # 인터넷문서 => 앱문서 => html ( 하이퍼텍스트 마크업 언어 )

from bs4 import BeautifulSoup as bs # html 언어 일어주는 함수 제공
import urllib.request as ur

# 1. 크롤링 할 인터넷주소 넣기
url = 'https://movie.naver.com/movie/running/current.nhn'

# 2. 주소 열어서 앱문서 변수에 저장
앱문서 = ur.urlopen( url )

# 3. 애문서 변수 읽기
soup = bs(앱문서.read() , 'html.parser')

# 4. 해당 태그를 찾아서 가져오기
태그 = soup.find_all( 'ul' , { "class" : "current_list" })

print( 태그 )

# 영화 랭킹 크롱링 하기

주소 = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
앱문서 = ur.urlopen( 주소 )
soup = bs( 앱문서.read() , 'html.parser')
태그 = soup.find_all( 'div' , {"class" : "tit3"})
print( 태그 )
