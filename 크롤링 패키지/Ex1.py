# 정보수집_크롤링 패키지
    # 1. Ex1.py

# 크롤링 : 인터넷에서 데이터 추출하기
    # 인터넷문서 => 앱문서 => html ( 하이퍼텍스트 마크업 언어 )

from bs4 import BeautifulSoup as bs
import urllib.request as ur

url = 'https://quotes.toscrape.com/' # 1.인터넷 주소

html = ur.urlopen( url ) # 2. 인터넷주소 파이썬으로 가져오기

soup = bs(html.read(), 'html.parser' ) # 3. read() : 인터넷 읽어오기

print( soup.find_all('span')[0].text) # 4. 읽어온 파일중 찾기('span') 찾아서 첫번째 텍스트 가져오기
# 마크업언어[html] 에서 <span> 태그를 찾아서 태그 사이에 있는 텍스트를 가져오기

print( soup.find_all('span')[1].text)

print( soup.find_all('span')[2].text)

print( soup.find_all('span')[4].text)

# 모든 span 출력
for i in soup.find_all('span') :
    print(i.text)
# span에 포함된 해당 클래스만 찾기
for i in soup.find_all( 'div' , {"class" : "quote"} ) :
    print(i.text)