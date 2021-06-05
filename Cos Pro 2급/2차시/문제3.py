# 문제 3

import math

def soiution( N , M ) :
    total = 0
    for x in range( N , M+1 ) :
        if x % 2 == 0 :
            total += x+x

    return total

N = 4
M = 7

ret = soiution( N , M )
print("solution 함수의 변환 값은 " , ret , "입니다")