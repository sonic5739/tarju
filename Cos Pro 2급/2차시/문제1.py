# 문제1
max_product_number = 10

def fun_c( gloves ) :
    counter = [0 for _ in range(max_product_number + 1)]
    # counter = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
    for x in gloves :
        counter[x] += 1
    return counter

# 순서도 : [ , 1 , 2 , 2 , 2 , 4 ]
# count [ 1 , 3 , 0 , 1, 0 , 0 , 0 , 0 , 0 , 0 ]
# 순서도 : [ 1 , 2 , 2 , 4 , 4 , 7 ]
# count : [ 1 , 2 , 0 , 2 , 0 , 0 , 1 , 0 , 0 , 1 ]

def soiution( left_gloves , right_gloves ) :
    left_counter = fun_c(left_gloves)
    right_counter = fun_c(right_gloves)

    total = 0
    for i in range(1,max_product_number + 1 ) :
        total += min(left_counter[i],right_counter[i])
    return total

left_gloves = [ 2 , 1 , 2 , 2 , 4 ]
right_gloves = [ 1 , 2 , 2 , 4 , 4 , 7]
ret = soiution(left_gloves,right_gloves)

print("solution 함수의 변환 값은 " , ret , "입니다")