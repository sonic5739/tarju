# 문제 71
my_variable = ( ) # 튜플 생성
# 문제 72
movie_rank = ("닥터 스트레인지","스플릿","럭키")
# 문제 73
my_tuple = ( 1 )
print( type(my_tuple) ) # int 정수 # 튜플이아니다
my_tuple = ( 1 , ) # , 추가
print( type(my_tuple) ) # tuple # 튜플로 생성
# 문제 74
# t = (1,2,3)
# t[0] = 'a' # 0번째 순서의 값을 a로 변환
# 오류발생 이유 = 튜틀은 값을 바꿀수 없다
# 문제 75
t =  1 , 2 , 3 , 4
print( type(t))
# t의 타입은 튜플이다
# 문제 76
# t = ('a','b','c')
# t[0] = "A"
# 튜틀은 수정이 불가하다
# 문제 77
interest = ('삼성전자','LG전자','SK Hynix')
print( list(interest ) )
# list( 튜플 ) : 리스트로 변환
# 문제 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest ) )
# 문제 79
temp = ('apple','banana','cake')
a , b , c = temp
print( a , b , c )
# apple banana cake
# 문제 80
data = tuple( range(2,100,2) )
print( data )
# range( 시작값 , 끝값 , 증가단위 )