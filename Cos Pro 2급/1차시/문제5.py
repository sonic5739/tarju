# 문제 5
def solution(arr):
    left, right = 0, len(arr)-1
    # 왼쪽 = 0 , 오른쪽 = 0
    while left < right :
        arr[left],arr[right] = arr[right], arr[left]
            # 첫번째값[왼] , 첫번째값[오른] = 첫번째값[오른] , 첫번째값[왼]
        left += 1 # 왼쪽 1 증가
        right -= 1 # 오른쪽 1 감소
    return arr

    # left가 0일 경우 right도 0이다 => 반복문 실행
        # arr[0] , arr[0] = arr[0] , arr[0]
        #  1         1       1        1
        # left+1   right-1
    # left = 1  right = -1
        # arr[1] , arr[-1] = arr[-1] , arr[1]
        #  4        3          3        4
        # left+1  right-1
    # left 2 일경우 right -2
        # arr[2] , arr[-2] = arr[-2] , arr[2]
        #  2        2          2        2

arr = [1, 4, 2, 3]
ret = solution(arr)

print("solution : return value of the function is", ret , ".")