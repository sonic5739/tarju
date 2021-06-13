def solution(words, word):
    count = 0
    sonic = 0
    for i in words :
        for b in range(4) :
            if word[b] != i[b] :
                count += 1
        sonic = 0
    return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")