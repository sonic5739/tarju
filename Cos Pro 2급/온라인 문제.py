# 문제 1
def func_a(k):
    sum = 0 # 누적합계 변수
    for i in range(k+1):
    # for변수 in range(~~~전까지) : 변수는 1부터 ~~ 전까지 1씩 증가하면서 반복
        # i는 1부터 k전까지 반복
    # i는 1부터 K+1 전까지 반복
        sum += i # i에 sum을 저장
    return sum

def solution(n, m):
    sum_to_m = func_a(m) # 1단계
    sum_to_n = func_a(n-1) # 2단계
    answer = sum_to_m - sum_to_n # 3단계
    return answer
# 문제 2
def func_a(s): # 점수리스트를 너어서 최댓값 구하기
    ret = 0 # 최댓값 0으로 설정
    for i in s: # 점수 리스트에 하나씩 i 대입
        if i > ret: # i 가 최댓값보다 크면
            ret = i  # i는 최댓값에  저장
    return ret

def func_b(s): # 점수리스트에 넣어서 합계 구하기
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s): # 정수리스트에 넣어서 최솟값구하기
    ret = 101 # 최솟값을 101로 설정
    for i in s: # 점수리스트에 하나씩 i 대입
        if i < ret: # i가 최솟값보다 작으면
            ret = i # i는 최솟값 저장
    return ret

def solution(scores):
    sum = func_b(scores) # 1 단계
    max_score = func_a(scores) # 2 단계
    min_score = func_c(scores) # 3 단계
    return sum - max_score - min_score # 4 단계
# 문제 3
def func_a(arr, n): # 1번에서 제외한 나머지 값들도 세로
    # arr : visitor
    # n = max_first
    ret = [] # 새로운 리스트
    for x in arr: # 방문객리스트에 하나씩 x대입
        if x != n: # x가 최대방문객수와 다르면
            ret.append(x) # 새로운 리스트에 저장
    return ret

def func_b(a, b): # 첮번째 방문객수와 두번째 방문객 수
    # a = max_first
    # b = max_second
    if a >= b:
        return a - b # 빼기 = 차이
    else:
        return b - a # 빼기 차이

def func_c(arr): # 방문객 리스트에서 가장많은 방문객수를  구하는 함수
    ret = -1 # 최댓값능 -1로 설정
    for x in arr: # 방문객리스트에서 하나씩 x에 대입
        if ret < x: # x가 최댓값보다
            ret = x # x는 최댓값에 저장
    return ret

def solution(visitor):
    max_first = func_c(visitor) # 1단계
    visitor_removed = func_a(visitor,max_first) # 2단계
    max_second = func_c(visitor_removed) # 3단계
    answer = func_b(max_first,max_second)
    return answer
# 문제 4
def solution(scores):
    grade_counter = [0 for i in range(5)]
    # grade_counter : 학점목록에 학점[k-5]를 설정
    for x in scores: # 점수목록에서 x에 하나씩대입
        if x >= 85: # x가 85점이상이면
            grade_counter[0] += 1 # 학생목록[0] = a학점 학생 한명 추가
        elif x >= 70: # x가 70점이상이면
            grade_counter[1] += 1 # 학생목록[1] = b학점 학생 한명 추가
        elif x >= 55: # x가 55점이상이면
            grade_counter[2] += 1 # 학생목록[2] = c학점 학생 한명 추가
        elif x >= 40: # x가 44점이상이면
            grade_counter[3] += 1 # 학생목록[3] = d학점 학생 한명 추가
        else: # 그외
            grade_counter[4] += 1 # 학생목록[4] = e학점 학생 한명 추가
    return grade_counter
# 문제 5
def solution(stones): # stone = 징검다리에 있는 적혀있는 수의 리스트
    cnt = 0 # 점프한 개수
    current = 0 # 현재 개구리의 위치
    n = len(stones) # 징검다리의  개수 = len(리스트)
    while current < n: # 현재위치가 징검다리개수보다 작으면
        # 현재위치가 마지막징검다리까지 반복
        current += stones[current]
        # 개구리 현재위치에 더해주기
        cnt += 1 # 점프수 증가
    return cnt # 점프수 반환환
# 문제6
def solution(height, k):
    answer = 0 # k보다 큰 수의 개수
    n = len(height) # 키의 목록 개수
    for h in height: # 키 리스트를 하나씩 h에 대입
        if h > k: # k가 h보다 작으면
            answer += 1 # k보다 큰 수의 변수에 +1
    return answer
# 문제 7
def solution(s): # s : 문자 abz
    s_lst = list(s)
    n = len(s) # n = 문자열개수
    for i in range(n): # 문자열 개수 반복
        if s_lst[i] == 'a': # 만약에 리스트에[i] == 'a' 이면
            s_lst[i] = 'z' # z로 변경
        elif s_lst[i] == 'z': # 만약에 리스트에[i] == 'z' 이면
            s_lst[i] =  'a' # a로 변경
    return "".join(s_lst) # ""뒤에 문자열 붙이기기
# 첫번째 IF가 T  이더라도 두번째 IF도 검사 실행
# if 조건1 :
# if 조건2 :

# 두번째 IF가 T 이면 두번째 elif는 검사 안함
# if 조건1 :
# elif 조건2 :
# 문제 8
def solution(name_list): # 학생들의 이름 목록
    answer = 0 # 이름에 k , j 가 포함되어 있는 학생수
    for name in name_list: # 학생목록에 하나씩 n에 대입
        for n in name: # name에 문자 하나씩 n에 대입
            if n == 'j' or n == 'k': # 해당 문자가 j 또는 k 이면
                answer += 1 # 구하는 학생수에 + 1
                # continue는 가장 가까운 반복문으로 이동
                # j 또는 k를 찾았으면 다시 학생이름 으로 이동
                break
    # continue : 가장 가까운 for 다시 실행
    # break : 가장 가까운 for 종료
    return answer
# 문제 9
# 거스름돈 구하기
# 지불한금액 - 총구매한 가격
def solution(price, money):
    # price : 구매한 가격들의 리스트
    # money : 지불한 금액
    answer = money - sum(price)
        # sum(리스트) : 리스트내 요소들의 전체 합계
    # answer : 거스름돈
    # 만약에 지불한 금액보다 구매할 총구매금액이 더 크면
    if answer < 0 : # 만약에 거스름돈이 마이너스이면
        answer = -1 # -1 리턴
    return answer
# 문제 10
def solution(arr, k):
    # arr : 2차원 리스트
    # k : k번쩨 작은수
    answer = 0 # k번째 작은수
    리스트 = [] # 임시 리스트
    n = len(arr) # n은 배열의 세로길이
    for 세로 in range(n) :
        for 가로 in range(4) : # 4는 배열의 가로길이
            리스트.append(리스트[세로][가로])
            # 2차워리스트 값을 1차원리스트에 저장
    # 정렬 => sort : 오름차순으로 정렬하기
    리스트.sort()
    # k번째 => 인덱스 [k-1] : 이유 : 인덱스는 0번부터 시작
    answer = 리스트[k-1]
    return answer