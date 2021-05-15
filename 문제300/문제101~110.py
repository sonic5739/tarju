# 논리 : 맞는지 틀린지 판단
# 연산자 :
    # 산술연산자 : + 더하기 -빼기 *곱하기 /나누기 // 나누기[몫] % 나누기[나머지]
    # 비교연산자 : > 초과 < 미만 >= 이상 <= 이하 == 같다 != 같지 않다
    # 논리연산자 : and [ 이면서 ] or [ 이거나 ] ![부정]
    # 대입연산자 :   = [오른쪽값을 왼쪽값에 빼기 후 왼쪽값에 대입

      # IF : 논리문
      #   if 논리 :
      #       참 [코드]
      #   else:
      #       거짓 [ 코드]

      # if 논리 :
      #     참 [코드]
      # elif 논리2:
      #     참2[코드2]
       # elif 논리3:
       #     참3[코드3]
       # else:
     #     거짓[코드]

      # if 논리 :
      #     참 [ 코드 ]
      # if 논리2
      #     참2 [코드2]
      # if 논리3 :
      #     참3 [ 코드3 ]

      # if 논리 :                        if 학년 = 3 :
      #     if 논리 :                           if 성별=남
      #         참 [ 코드 ]                        학년이 3 아니면서 남학생
      #     else:                              else :
      #         거짓 [ 코드 ]                      학년이 3 아니면서 여학생
      # else:                           else :
      #     if 논리:                            if 성별=남
      #         참[코드]                           학년이 3 아니면서 남학생
      #     else:                              else :
      #         거짓[코드]                         학년이 3 아니면서 여학생

# 문제 101 : type() : 데이터의 타입[형태] 확인해주는 함수
print( type(True) ) # bool : 참[True] 거짓[False] 들중 하나 저장하는 타입
print( type(False) ) # bool : 참[True] 거짓[False] 들중 하나 저장하는 타입
# 문제 102
print(3==5)
# False
# 문제 103
print( 3 < 5 )
# True
# 문제 104
x = 4
print(1 < x < 5 )
# True
# 문제 105
print( (3==3) and (4 != 3) )
# True
# 문제 106
# print(3 => 4)
# 3은 4의 이상이 아니라 이하이다
# 문제 107
if 4 < 3 :
    print("Hello World")
# 아무것도 출력되지 않는다
# 문제 108
if 4 < 3 :
    print("Hello World")
else:
    print("Hi, there")
# HI< there만 출력된다
# 문제 109
if True :
    print("1")
    print("2")
else:
    print("3")
print("4")
# 1 , 2 , 4 가 추력된다
# 문제110
if True :
    if False :
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
# 3, 5 가 출력 된다