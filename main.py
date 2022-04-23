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
file = open("words.txt",'w')
file.write('anonymously\n''compatibility\n''dashboard\n''experience\n''photography\n''spotlight\n''warehouse\n')
file.close()
file = open("words.txt",'r')
s = file.read()
print(s)
file.close()
# write를 사용해서 문자열을 쓸수있다

