# 문제 31
# a = "3" 3+4=7이 아니라 30+4인  34가 나올것이다
# b = "4"
# print( a + b )
# 문제 32 HI 가 3번 나온다
# print("HI" * 3)
# 문제 33
print('-'*80)
# 문자 34
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print( t3 * 4 )
# 문제 35 : farmat : 형식 farmatting : %
# %s : 문자 형식 % : 정수 형식
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 %d" % ( name1 , age1 ) )
print("이름 : %s 나이 %d" % ( name2 , age2 ) )
# 문제 36 farmat
# {}안에 들어갈 데이터를 farmat 함수 아네 넣기
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : {} 나이{}".format(name1,age1))
print("이름 : {} 나이{}".format(name2,age2))
# 문제 37 : f-string : f"문자{변수명}
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print( f"이름 : {name2} 나이 : {age2}")
print( f"이름 : {name1} 나이 : {age1}")
# 문제 38
상장주식수 = "5,969,782,550"
상장주식수2 = 상장주식수.replace(",", "")
타입변환 = int( 상장주식수2 )
print(타입변환)
# 문제 39
분기 = "2020/03(E) (IFRS연결)"
print( 분기[ 0 : 7 ] )
# 문제40 공백을제거하는 함수 strip( )
data = "          삼성전자           "
공백제거 = data.strip()
print( 공백제거 )