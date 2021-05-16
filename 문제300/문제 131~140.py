# 반복문
# 1. FOR 변수명 IN 리스트명 : 리스트내 모든 변수를 하나씩 변수명에 대입
# 2. for 변수 in range( 시작값 , 끝값 , 증감단위 ) : 시작값 부터 끝값까지 증감하면서 변수명에 하나씩 대입
    # range( 값 ) : 값 만큼 반복 실행
    # range( 시작값 , 끝값 ) : 시작값 부터 끝값 전까지 1씩 증가하면서 반복
    # range( 시작값 , 끝값 , 증감단위 ) : 시작값 부터 끝값까지 증감하면서 변수명에 하나씩 대입

# 2 ~ 9 구구단
# for 단 in range(2,10) : # 2부터 9까지 1씩 증가 하면서 단에 하나씩 대입
    # for 곱 in range( 1 , 10 ) : # 1부터 9까지 1씩 증가 하면서 곱에 하나씩 대입
         # print( 단 , " x " , 곱 , "=" , (단 * 곱) )
# 단은 8번 반복 : 곱은 단이 1씩 증가항때마다 9번씩 반복 = 72번 반복
# 피라미드 만들기
# for sonic in range( 1 , 6 ) :
#     print( " "*(6-sonic) , "*"*(2*sonic-1) )

# 피라미드 알고리즘
#       *             1줄    =       공백 4개               별1개
#      ***            2줄    =       공백 3개               별3개
#     *****           3줄    =       공백 2개               별5개
#    *******          4줄    =       공백 1개               별7개
#   *********         5줄    =       공백 0개               별9개
#                    1씩증가         1씩감소                2개씩증가
#                               최대줄수 - 현재줄수           현재줄수*2+1
#                 range( 1 , 6 )    " "*(6-변수)       "*"*(2*변수-1)

# 문제 131
과일 = ["사과","귤","수박"]
for 변수 in 과일 :
    print(변수)
# 사과
# 귤
# 수박
# 문제 132
과일 = ["사과","귤","수박"]
for 변수 in 과일 :
    print("#####")
# #####
# #####
# #####
# 문제 133
# 알파벳 = ["A","B","C"]
# for 변수 in 알파벳 :
#     print(변수)
변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)
# 문제 134
# 알파벳 = ["A","B","C"]
# for  변수 in 알파벳 :
#     print("출력 : " , 변수)
변수 = "A"
print("출력 : ",변수)
변수 = "B"
print("출력 : ",변수)
변수 = "C"
print("출력 : ",변수)
# 문제 135
변수 = "A"
print("변환 : ",변수.lower())
변수 = "B"
print("변환 : ",변수.lower())
변수 = "C"
print("변환 : ",변수.lower())
# 문제 136
숫자 = [10,20,30]
for 변수 in 숫자 :
    print(변수)
# 문제 137
숫자 = [10,20,30]
for 변수 in 숫자 :
    print(변수)
# 문제 138
숫자 = [10,20,30]
for 변수 in 숫자 :
    print(변수)
    print("-------")
# 문제 139
print("++++")
for 변수 in [10,20,30] :
    print(변수)
# 문제 140
for 변수 in [ 1 , 2 , 3 , 4 ] :
    print("-------") # 리스트내 개수만큼 반복 = 총 4번 출력
