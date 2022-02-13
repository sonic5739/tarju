# m = int(input("돈이 얼마나 있으십니까?"))
# h = input("배가 고프싶니까?(고프면yes아니면 no)")
# if m >= 10000 and h == "yes" :
#     print("저녘을 사먹으십시오")
# else :
#     print("집에서 먹으세요")
# a = 0
# while a < 10 :
#     a =a+1
#     print("나무가 %d번 찍혔습니다." %a)
# for a in range(1,11) :
#     print("나무가 %d번 찍혔습니다." % a)
# while True :
#     print("안녕하세요")
#     break # 즉시 반복문을 종료시키는 명령어
# a = 0
# while True :
#     a = a + 1
#     print(a)
#     if a ==100 :
#         break
# import random
# print('>>숫자 마추기 게임<<')
# com = random.randint(1,10)
# while True :
#     my = int(input("예상 숫자를 입력하시오 : "))
#     if com == my :
#         print("~~성공~~")
#         break
#     elif my > com :
#         print("더 작은수를 입력하세요")
#     else :
#         print("더 큰수를 입력하세요")
# a = 0
# while a < 100 :
#     a = a+1
#     if a % 2 == 0 :
#         continue
#     print(a)
# l = ["one","two","three"]
# for i in l :
#     print(i)
# a = 0
# b = 0
# l = [90,25,67,45,80]
# for i in l :
#     a = a+1
#     b = b+1
#     if i > 60 :
#         print("%d번째 학생은 합격입니다."%a)
#     else :
#         print("%d번째 학새은  불합격입니다"%b)
# a = 0
# l = ['b','b','ab','a','b','b','a']
# for i in l :
#     a = a+1
#     if i == 'a' :
#         print("%d번째 고객이 당첨되셨습니다"%a)
#         break
# a = 0
# for i in range(1,101) :
#     a += i
# print(a)
# a = 0
# print("수열 : ",end = ' ')
# for i in range(1,101) :
#     if (i % 3 == 0) and (i % 2 != 0) :
#         print("%d"%i, end= ' ')
#         a = a + i
# print("\n누적합 : %d" % a)
# import turtle
# for i in range(100) :
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(-60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(60)
#     turtle.forward(100)
#     turtle.right(100)
#     turtle.forward(30)
# for i in range(2,10) :
#     print("%d단 입니다"%i)
#     for a in range(1,10) :
#         print("%d x %d = "%(i,a),a*i) # print("%d x %d = %d",%(a,i,a*i))로도 표현 할수있다.
# l = []
# for i in range(1,101) :
#     if i % 3 == 0 :
#         l.append(i)
# print(l)
# a = [10,8,20,31,5]
# max = a[0]
# min = a[0]
# for i in a :
#     if min > i :
#         min = i
#     if max < i :
#         max = i
# print(max)
# print(min)
