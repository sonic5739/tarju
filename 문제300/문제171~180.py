# for 변수 in 리스트명 :
# for 변수 range( 시작값 , 끝값 , 증가단위 ) :

# 문제 171
list = [32100,32150,32000,32500]
for sonic in list :
    print( sonic )
# 문제 172
list = [32100,32150,32000,32500]
for i , sonic in enumerate(list) :
    print( i , sonic )
# 문제 173
list = [32100,32150,32000,32500]
for i in range( len(list)) :
    print( 3-i , list[i] )
# 문제 174
list = [32100,32150,32000,32500]
for i in range( 1 , 4 ) :
    print( 90+10 * i,list[i])
# 문제 175
my_list = ["가","나","다","라"]
for sonic in range( 1 , 4 ) :
    print( my_list[sonic-1] , my_list[sonic] )
# 문제 176
my_list = ["가","나","다","라","마"]
for sonic in range( 0 , 3 ) :
    print(my_list[sonic] , my_list[sonic+1],my_list[sonic+2] )
# 문제 177
my_list = ["가","나","다","라"]
print( my_list[3] , my_list[2])
print( my_list[2] , my_list[1])
print( my_list[1] , my_list[0])
# 문제 178
my_list = [ 100 ,200 , 400 , 800 ]
print(my_list[1] - my_list[0])
print(my_list[2] - my_list[1])
print(my_list[3] - my_list[2])
# 반복문
for i in range( 3 ) :
    print( my_list[i+1] - my_list[i])
# 문제 179
my_list = [ 100 , 200 , 400 , 800 , 1000 , 1300 ]
for i in range( 4 ) :
    print( (my_list[i] + my_list[i+1] + my_list[i+2] / 3 ) )
# 문제 180
저가 = [ 100 , 200 , 400 , 800 , 1000 ]
고가 = [ 150 , 300 , 430 , 880 , 1000 ]

저장리스트 = []
for i in range( 5 ) :
    저장리스트.append( 고가[i] - 저가[i] )
