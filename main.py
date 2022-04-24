# n = int(input())
# a = list(map(int,input().split()))
# y = 0
# m = 0
# for i in a :
#     y += (i // 30 * 10 + 10 )
#     m += (i // 60 * 15 + 15 )
# if y < m :
#     print('Y',y )
# if m < y :
#     print('M', m)
# if m == y :
#     print('Y','M',m)
# while True :
#     n = input()
#     if n == '0' :
#         break
#     print(n.count('1') * 2 + n.count('0') * 4 + (len(n) - n.count('1') - n.count('0')) * 3 + len(n) + 1)
# a,b = map(int,input().split())
# a = a - 1
# b = b - 1
# x1 = a //4
# x2 = b//4
# y1 = a%4
# y2 = b%4
# if x1 > x2 and y1 > y2:
#     print(x1-x2 + y1- y2)
# if x1 < x2 and y1 > y2:
#     print(x2-x1 + y1- y2)
# if x1 > x2 and y1 < y2:
#     print(x1-x2 + y2- y1)
# if x1 < x2 and y1 < y2:
#     print(x2-x1 + y2- y1)
# if x1 < x2 and y1 == y2:
#     print(x2-x1)
# if x1 > x2 and y1== y2:
#     print(x1 - x2)
# file = open("words.txt",'w')
# file.write('anonymously\n''compatibility\n''dashboard\n''experience\n''photography\n''spotlight\n''warehouse\n')
# file.close()
# file = open("words.txt",'r')
# s = file.read()
# print()
# file.close()
# write를 사용해서 문자열을 쓸수있다
#
# N = int(input())
# if N == 0 :
#     print("divide by zero")
# else:
#     print("1.00")
# N, M, K = map(int,input().split())
# 앞면x = N-M
# 뒷면x = N-K
# # print(min(M,K) + min(앞면x,뒷면x))
# a = int(input())
# b = int(input())
# print(2*a + 2 * 3.141592 * b)
# n = int(input())
# 답 = 0
# if n//2%2 == 0 :
#     답 = 2
# elif n%2 == 1:
#     답 = 0
# else:
#     답 = 1
# print(답)
# def divide(a,b) :
#     return a//b, a%b
# c,d = divide(5,2)
# print(c)
# e,f = add_sub(10,6)
# print
# def operate(10,3,'+')