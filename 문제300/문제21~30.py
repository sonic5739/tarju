# 문제 21
letters = 'python'
print( letters[0] , letters[2] )
# 문제 22
license_plate = "24가 2210"
print( license_plate[-4:] )
print( license_plate[4:8] )
# 문제 23
string = "홀짝홀짝홀짝"
print( string[ 0 : 6 : 2 ])
# 문제 24
string = "PYTHON"
print( string[ : : -1 ])
# 문제 25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace( "-" , " ")
print( phone_number1 )
# 문제 26
phone_number = "010-1111-2222"
phone_number2 = phone_number.replace( "-" , "" )
print( phone_number2)
# 문제 27 : split 자르다 분리 함수
url = "htts://sharebook.kr"
url_split = url.split(".") # .[점] 기준으로 자르기
print(url_split[1])
# 문제 28 : 예상 : 문자열 일부분 수정 불가
# lang = "python"
# lang[0] = "P"
# print(lang)
# 문제 29 : replaace 교체 함수
string = "abcdfe2a354a32a"
string =  string.replace( "a" , "A")
# 문제 30 : 예상 : 오류가난다 그이유 replace다음에 있는 괄호에 b와B가 " "가 아니라 ''이기 때문이다
# string = "abcd"
# string.replace('b','B')
# print(string)