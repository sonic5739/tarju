def func_a(scores, score): # scores , score 를 담는 함수 만들기
    rank = 1 # 순위를 1로 결정하기
    for s in scores: # score 리스트를 s에 넣어서 반복하기
        if s == score: # 만약 score 와 s 의 값이 갔다면
            return rank # rank 반환하기
        rank += 1 # rank를 1로 설정하기
    return 0 # 0을 반환하기

def func_b(arr): #
    arr.sort(reverse=True)

def func_c(arr, n):
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