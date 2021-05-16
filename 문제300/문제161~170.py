# 문제 161
for sonic in range(0 , 100 , 1 ) :
    print( sonic )
# 문제 162
for sonic in range( 2008 , 2051 , 4 ) :
    print( sonic )
# 문제  163
for sonic in range( 3 , 31 , 3) :
    print( sonic )
# 문제 164
for sonic in range(99 , -1 , -1 ) :
    print( sonic )
# 문제 165
for sonic in range( 0 , 10 , 1 ) :
    print("0.",sonic )
# 문제 166
for sonic in range( 1 , 10 ) :
    print("3 X ",sonic, " = ", 3*sonic)
# 문제 167
for sonic in range( 1 , 10 ) :
    if sonic%2 == 1  : # 만약에 변수가 홀수이면
        print( 3 ," X ",sonic, " = ", 3*sonic )
# 홀수/짝수 : 값%2 == 0
# 짝수 //  값%2 == 1 홀수
# 배수
# 값 % 수 == 0 : 나머지가 0이면 그값 은 그의 수의 배수
# 문제 168
합계 = 0
for sonic in range( 1 , 11 ) :
    합계 += sonic
print("누적합계 : " , 합계)
# 문제 169
합계 = 0
for sonic in range( 1 , 11 ) :
    if sonic % 2 == 1 :
        합계 += sonic
print("홀수 누적합계 : ", 합계)
# 170
누적합 = 1
for sonic in range( 1 , 11 ) :
    누적합 *= sonic
print("누덕 합게 : ", 누적합)