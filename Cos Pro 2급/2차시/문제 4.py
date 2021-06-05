# 문제 4

import math

def soiution(words) :
    answer = ''
    for w in words :
        if len(w) >= 5 :
            answer += w

    if len(answer) < 1 :
        answer = 'empty'
    return answer

words1 = ["my","favorite","color","is","vioiet"]
ret1 = soiution(words1)

print("solution 함수의 변환 값은 " , ret1 , "입니다")

words2 = [ "yes" , "it" , "is" ]
ret2 = soiution(words2)

print("solution 함수의 변환 값은 " , ret2 , "입니다")