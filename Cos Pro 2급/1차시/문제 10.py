# 문제 10
def soiution( data ) :
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for i in data :
        if i <= average :
            cnt += 1
    return cnt

data1 = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
ret1 = soiution(data1)
print("soiution1 함수 결과 " , ret1)

data2 = [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 10 ]
ret2 = soiution(data2)
print("soiution1 함수 결과 " , ret2)