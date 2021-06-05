# 팰린드롬 : noon : 첫번째 글자 == 마지막 글자'
# racecar : 두번째 글자 == 마지막앞글자
# 문제 8
def soiution( sentence ) :
    str = ''
    for c in  sentence : # 해당 문장을 문자 하나식 c 대입
        # if c != '.' or c != ' ' : # 문자가 . 아니거나 공백이 아니면
        if c != '.' and c != ' ':  # 문자가 . 이면서 공백이면
            str += c # str 에 문자 저장
    size = len(str) # 합쳐진 문자 길이 구하기
    for i in range( size // 2 ) : # // : 몫 문자길이//2
        if str[i] != str[size -1  - i ] : # 첫문자와 마지막문자가 다를 경우
            return False # 팰린드롬 X
    return True # 팰린드롬 0

sentence1 = "never odd or even"
ret1 = soiution( sentence1 )
print("soiution1 함수 결과 " , ret1)

sentence2 = "palindrome"
ret2 = soiution( sentence2 )
print("soiution2 함수 결과 " , ret2)