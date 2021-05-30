import urllib.request
import json
import re

def 네이버검색( 카테고리 , 검색결과수) :

    ClientID = 'O7Pg94YPM2lKlLGRptPP'
    ClientSecret = 'ykyhwzVaiS'
    url = "https://openapi.naver.com/v1/search/"+ 카테고리+".json"
    option = "&display="+검색결과수+"&sort=count"
    query = "?query="+urllib.parse.quote( input( 카테고리+"의 검색 정보 입력 : "))
    url_query = url + query + option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id", ClientID)
    request.add_header("X-Naver-Client-Secret", ClientSecret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)

    검색결과 = response_body.decode('utf-8')  # 한글 지원
    json결과 = json.loads(검색결과)
    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("---->검색결과 : " + 타이틀)


        if 카테고리 == "movie" :
            print("-------> 평점 : ", i["userRating"])
        if 카테고리 == "movie" :
            print("-------> 배우 : ", i["actor"])
        if 카테고리 == "movie" :
            print("-------> 감독 : ", i["director"])

        if 카테고리 == "book":
            print("-------> 저자 : ", i["author"])
        if 카테고리 == "book":
            print("-------> 출판사 : ", i["publisher"])

        if 카테고리 == "shop":
            print("-------> 제조사 : ", i["maker"])
        if 카테고리 == "shop":
            print("-------> 브랜드 : ", i["brand"])




# 프로그램  코드
while True : # 무한반복하기
    print( "검색[naverAPI] 프로그램 ")
    print( " 1.영화 " , "2.책" , "3.쇼핑")
    선택 = int( input("선택 : ") ) # 입력받아 선택변수에 저장
    if 선택 == 1:
        카테고리 = "movie"
        검색결과수 = input("-->영화 선택 했습니다. 몇개 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 2:
        카테고리 = "book"
        검색결과수 = input("-->책 선택 했습니다. 몇개 출력할까요? ")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 3:
        카테고리 = "shop"
        검색결과수 = input("-->쇼핑 선택 했습니다. 몇개 출력할까요? ")
        네이버검색(카테고리, 검색결과수)

    if 선택 == 0 :
        print("--> 이용해주셔서 감사합니다")
        break
