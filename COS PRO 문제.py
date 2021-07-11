# 문제 1
def solution(셔츠사이즈) :
    조사결과리스트 = [ 0 , 0 , 0 , 0 , 0 , 0 ]
    for 셔츠 in 셔츠사이즈 :
        if 셔츠 == "XS":
            조사결과리스트[0] += 1
        if 셔츠 == "S":
            조사결과리스트[1] += 1
        if 셔츠 == "M":
            조사결과리스트[2] += 1
        if 셔츠 == "L":
            조사결과리스트[3] += 1
        if 셔츠 == "XL":
            조사결과리스트[4] += 1
        if 셔츠 == "XXL":
            조사결과리스트[5] += 1
    return 조사결과리스트
셔츠사이즈 = ["XS","S","L","L","XL","S"]
print(" 조사 결과 : ", solution(셔츠사이즈) )

# 문제 2
def solution( 가격 , 등급 ) :
    할인전용가 = 0
    if 등급 == "S" :
        할인전용가 = int(가격 * 0.95)
    if 등급 == "G" :
        할인전용가 = int(가격 * 9)
    if 등급 == "V" :
        할인전용가 = int(가격 * 0.85)
    return 할인전용가

가격1 = 2500
등급1 = "V"
print(" 조사 결과 : ", solution(가격1,등급1) )

가격2 = 96900
등급2 = "S"
print(" 조사 결과 : ", solution(가격2,등급2) )

# 문제 3
def solution( 시작번호 , 끝번호 ) :
    합 = 0
    for 번호 in range(시작번호,끝번호) :
        if 번호 % 2 == 0 :
            합 += 번호*번호

    return 합
시작번호 = 4
끝번호 = 7
print(" 조사 결과 : ", solution( 시작번호 , 끝번호 ) )

# 문제 4
def solution(단어목록) :
    결과 =""
    for 단어 in 단어목록 :
        if len(단어) == 5 :
            결과 += 단어
    if len(결과) < 1 :
        결과 = "empty"

    return 결과

단어목록1 = ["my","favorite","color","is","violet"]
print("조사 결과 : ",solution(단어목록1))
단어목록2 = ["yes","i","am"]
print("조사 결과 : ",solution(단어목록2))

# 문제 5
def solution(점수목록) :
    평균 = 0
    평균 = (sum(점수목록)-max(점수목록)-min(점수목록)) // ( len(점수목록)-2)
    return 평균
점수목록1 = [35,28,98,34,20,50,85,74,71,7]
print("조사 결과 : ",solution(점수목록1))
점수목록2 = [1,1,1,1]
print("조사 결과 : ",solution(점수목록2))
# 문제 6
def solution(단어목록 ) :
    오타수 = 0
    for 오타단어 in 단어목록 :
        for x , y in zip( 오타단어 , 단어 ) :
            if x != y :
                오타수 += 1
    return 오타수
단어목록 = ["CODE","COED","CDEO"]
단어 = "CODE"
# 문제 7
def solution(지형) :

    dx = [ -1 , 1 , 9 , 0 ]
    dy = [ 0 , 0 , -1 , 1 ]
    위험지역 = 0

    for 가로 in range(4) :
        for 세로 in range(4) :
            체크 = True
            for 지역 in range(4) :
                if 0 <=가로 +dx[지역] and 가로+dx[지역] < 4 and 0 <=세로 +dy[지역] and 세로 + dy[지역] < 4 :
                    if 지형[ 가로+dx[지역]][ 세로+dy[지역]] <=지형[가로][세로] :
                        체크 = False
            if 체크 :
                위험지역 += 1

    return 위험지역
지형 = [ [3,6,2,8] , [7,3,4,2] , [8,6,7,3] , [5,3,2,9] ]
print("현재 위험지역은 : ", solution(지형))
# 문제 8
def solution(점수목록) :
    합격자수 = 0
    for 점수 in 점수목록 :
        if 점수 >= 커트라인 :
            합격자수 += 1
    return 합격자수
점수목록 = [80,90,55,60,59]
커트라인 = 60
print("현재 합격자 수 : ", solution(점수목록))
# 문제 9
# 문제 10
def solution( 근무시간 , 근무자수 ) :
    최장시간 = 0
    리스트 = [ 0 for _ in range(근무자수) ]
    for 인덱스 , 시간 in enumerate( 근무시간 ) :
        리스트[인덱스 % 근무자수 ] += 시간
    최장시간 = max( 리스트 )
    return  최장시간
근무시간1 = [ 1 , 5 , 1 , 9 ]
근무자수1 = 3
print("가장오래말한 시간 :  ",solution(근무시간1,근무자수1))
근무시간2 = [ 4 , 8 , 2 , 5 , 4 , 6 , 7 ]
근무자수2 = 4
print("가장오래말한 시간 :  ",solution(근무시간2,근무자수2))
# 문제 11
def solution( 사이즈목록 ) :
    사이즈수 = [ 0 for _ in range(4) ]

    for 사이즈 in 사이즈목록 :
        if 사이즈 < 95 :
            사이즈수[0] += 1
        elif 사이즈 >= 95 and 사이즈 < 100 :
            사이즈수[1] += 1
        elif 사이즈 >=  100 and 사이즈 < 105 :
            사이즈수[2] += 1
        elif 사이즈 >= 105 :
            사이즈수[3] += 1
    return 사이즈수

사이즈목록 = [97,102,93,100,107]
print("조사 결과 : ",solution(사이즈목록))
# 문제 12
def solution( 카드목록 ) :
    총점수 = 0
    색상별카드 = [0 for _ in range(3)]
    for 카드 in 카드목록 :
        if 카드[0] == "black" :
            색상별카드[0] += 1
        if 카드[0] == "blue" :
            색상별카드[1] += 1
        if 카드[0] == "red" :
            색상별카드[2] += 1
        총점수 += int(카드[1])

    if 색상별카드[0] == 3 or 색상별카드[1] == 3 or 색상별카드[2] == 3 :
        총점수*=3
    elif 색상별카드[0] == 2 or 색상별카드[1] == 2 or 색상별카드[2] == 2:
        총점수*=2
    return 총점수
카드목록1 = [ ["blue" , "2"] , ["red" , "5"] , ["black" , "3"]]
print("카드목록의 총점수 : " , solution(카드목록1))
카드목록2 = [ ["blue" , "2"] , ["blue" , "5"] , ["black" , "3"]]
print("카드목록의 총점수 : " , solution(카드목록2))