# 문제 9
def soiution( characters ) :
    result = ""
    result += characters[0]
    for i in range( 1 , len(characters ) ) :
        if characters[i-1] != characters[i] :
            result += characters[i]


    return result

characters = "senteeeenccccceeee"
ret = soiution( characters )
print("soiution 함수 결과 " , ret )
