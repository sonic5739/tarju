# a = 0
# b = 0
# l = [90,25,67,45,80]
# for i in l :
#     a = a + 1
#     b = b+1
#     if i > 60 :
#         print("%d번째 학생은 합격입니다."%a)
#     if i < 60 :
#         print("%d번쨰 학생은 불합격입니다."%b)
# a = 0
# for i in range(1,101) :
#     a = a + i
# print(a)
# a = 0
# for b in range(2,10) :
#     for i in range(1,10) :
#         a = b * i
#         print("%d x %d = %d "%(i,b,a)
# l = [93,45,21,30,20,94,66,71,45]
# min = l[0]
# max = l[0]
# for i in l :
#     if i < min :
#         min = 0
#     if i > max :
#         max = i
# print(max)
# print(min)
# lst = [ 1 , 4 ]
# a = lst[0]
# lst[0] = lst[1]
# lst[1] = a
# print(lst)
# lst = [19,29,39403,40,30348403]
# a = lst[0]
# b = lst[1]
# c = lst[2]
# lst[0] = b
# lst[1] = c
# lst[2] = a
# print(lst)
# lst = [93,45,21,30,20,94,66,71,45] # 알고리즘
# for i in range(0,len(lst)-1) :
#     for j in range(i+1,len(lst)) :
#         if lst[i] > lst[j] :
#             a = lst[i]
#             lst[i] = lst[j]
#             lst[j] = a
# print(lst)
# 함수
# def sum(a,b) :
#     c = a+b
#     return c
# print(sum(3,4))
# def d(*args) :
#     c = 0
#     for i in args :
#         c = c + i
#     return c
#     print(d(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)) # ()안에 *땡땡을 넣으면 무한개로 들어간다
# def hello() :
#      print("hello python !")
# hello() # 이것은 함수를 호출하는 것이다.
# def hello() :
#      return "hello python !"
# print(hello())
# def sortlst(a) :
#     lst = a
#     for i in range(0, len(lst) - 1):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 a = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = a
#     return lst
# print(sortlst([20,30,11,2]))
# def hello(a) :
#     lst = [1,2,3,4,5,6,7]
#     b = 0
#     for i in lst :
#         b = b + 1
#         if i == a :
#             print("%d번째 입니다."%i)
# hello(3)
# def hello(a,b) :
#     lst = a
#     num = 0
#     for i in lst :
#         num += 1
#         if i == b :
#             print("%d번째 입니다."%num)
# hello([4,20,30,11,5],4)
# def hello(b) :
#     for i in range(2,10) :
#         for j in range(1, 10):
#             if i == b :
#                 print("%d단 입니다"%i)
#                 c = i * j
#                 print("%d x %d = %d" % (i, j, c))
# hello(4)
# def gugu(input) :
#     print("%d단 입니다."%input)
#     for right in range(1,10) :
#         print("%d x % d = %d "%(input,right,input*right))
# gugu(4)
# def maximize(lsta) :
#     l = lsta
#     max = l[0]
#     for i in l :
#         if i > max :
#             max = i
#     print(max)
# maximize([1,2,3,4,5,6,7,8,9,0,10])
# list = []
# def test(a) :
#     for i in range(1,101) :
#         if i % a == 0 :
#             list.append(i)
#     print(list)
# test(5)
# import turtle
# for i in range(12) :
#     turtle.forward(60)
#     turtle.right(30)
