# 문제 1
def func_a(scores, score): # scores , score 를 담는 함수 만들기
    rank = 1 # 순위를 1로 결정하기
    for s in scores: # score 리스트를 s에 넣어서 반복하기
        if s == score: # 만약 score 와 s 의 값이 갔다면
            return rank # rank 반환하기
        rank += 1 # 순위를 내리기
    return 0 # 0을 반환하기

def func_b(arr): # 내림차순 함수
    arr.sort(reverse=True) # 리스트.sort(reverse=True) : 오름차순 -> 내림차순

def func_c(arr, n): # n번학생의 점수
    return arr[n]

def solution(scores, n):
    score = func_c(scores,n)
    func_b(scores)
    answer = func_a(scores,score)
    return answer

scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3
ret = solution(scores, n)

print("solution 함수의 반환 값은", ret, "입니다.")

# 문제 2
def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade)
    count = 0
    for i in range(arr_length):
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
            count += 1
        elif current_grade[i] >= 80 and rank[i] == 1:
            count += 1
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            count += 1
    return count

def func_b(current_grade):
    arr_length = len(current_grade)
    rank = [1] * arr_length
    for i in range(arr_length):
        for j in range(arr_length):
            if current_grade[i] < current_grade[j]:
                rank[i] += 1
    return rank

def func_c(current_grade, last_grade):
    max_diff_grade = 1
    for i in range(len(current_grade)):
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_b(current_grade)
    max_diff_grade = func_c(current_grade,last_grade)
    answer = func_a(current_grade,last_grade,rank,max_diff_grade)
    return answer

current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

print("solution 함수의 반환 값은", ret, "입니다.")

# 문제 3
def solution(scores):
    anawer = 0
    scores.sort(reverse=True)
    for i in range(1,len(scores) -1 ) :
        anawer = scores[i]
    anawer = anawer / (len(scores) -2 )
    return int(anawer)

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")

# 문제 4
def solution(words, word):
    count = 0
    sonic = 0
    for i in words:
        for b in range(4):
            if word[b] != i[b]:
                count += 1
        sonic = 0
    return count


words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")

# 문제 5
def solution(member_age, transportation):
    if transportation == 'Bus':
        adult_expense = 40000
        child_expense = 15000
    elif transportation == 'Ship':
        adult_expense = 30000
        child_expense = 13000
    elif transportation == 'Airplane':
        adult_expense = 70000
        child_expense = 45000

    if len(member_age) >= 10:
        adult_expense = 0.9 * adult_expense
        child_expense = 0.8 * child_expense

    total_expenses = 0
    for age in member_age:
        if age >= 20:
            total_expenses += adult_expense
        else:
            total_expenses +=  child_expense

    return total_expenses


member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

print("solution 함수의 반환 값은", ret1, "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

print("solution 함수의 반환 값은", ret2, "입니다.")

# 문제 6
def solution(tile_length):
    answer = ''
    com = 'RRRGGB'
    if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 4 :
        answer = '-1'
    else:
        for i in range(tile_length):
            answer += com[i % 6]
    return answer

tile_length1 = 11
ret1 = solution(tile_length1)

print("solution 함수의 반환 값은 ", ret1, " 입니다.")

tile_length2 = 16
ret2 = solution(tile_length2)

print("solution 함수의 반환 값은 ", ret2, " 입니다.")

# 문제 7
def solution(num_apple, num_carrot, k):
    answer = 0

    if num_apple < num_carrot * 3 :
        answer = num_apple // 3
    else:
        answer = num_carrot

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer -= 1
        i = i + 1

    return answer

num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

print("solution 함수의 반환 값은", ret2, "입니다.")

# 문제 8
def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]) :
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i >= 2 :
            answer = answer + 1
    return answer

programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

print("solution 함수의 반환 값은", ret, "입니다.")

# 문제 9
def solution(day, numbers):
    count = 0
    for number in numbers:
        if number % 2 == day % 2:
            count += 1
    return count


day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

print("solution 함수의 반환 값은", ret, "입니다.")

# 문제 10
def solution(arr):
    answer = 0
    for i in arr:
        if i / 2 in arr:
            answer += 1
    return answer


arr = [4, 8, 3, 6, 7]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")