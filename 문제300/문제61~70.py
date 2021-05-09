# 문제 61 price 변수에는 날짜와 종가 정보가 저장되 있다
price = ['20180728',100,130,140,150,160,170]
print(price[ 1 : ])
# [ 슬라이싱 ] = [1 : ] = 2번째값붙터 끝까지
# 문제 62
nums = [1,2,3,4,5,6,7,8,9,10 ]
print(nums[ : : 2])
# [ 슬라이싱 ] = [ : : 2  ] = 0번째값부터 끝까지 2개씩 이동 = 0 2 4 6 8
# [ 시작번호 : 끝번호 : 이동단위]
# 문제 63
nums =  [1,2,3,4,5,6,7,8,9,10 ]
print(nums[1 : : 2])
# [ 슬라이싱 ] = [ 1 : : 2 ] = 1번째 값부터 끝까지 2개씩 이동 = 1 3 5 7 9
# 문제 64
nums = [1,2,3,4,5]
print(nums[ : : -1])
# [ 슬라이싱 ] = [ : : -1 ] = 뒤로 이동
# 문제 65
interest = ['삼성전자','LG전자','Naver']
del interest[1]
print(interest)
# 문제 66
interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print(" ".join(interest))
# 문제 67
interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print(",".join(interest))
# 문제 68
interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print("\n".join(interest))
# 문제 69
string = "삼성전자/LG전자/Naver"
print(string.split("/"))
# 문제 70
data = [2,4,3,1,5,10,9]
# 오름 차순
data.sort()
print(data)
# 내림 차순
data.sort(reverse=True)
print( data )