# 복습#############함수
# def maximise(input) :
#     sonic = input
#     max = sonic[0]
#     for i in sonic :
#         if i > max :
#             max = i
#     print(max)
# maximise([1,2,3,4,5,6,7,7,8,98])
# def sonic(a) :
#     lista = []
#     for i in range(1,101) :
#         if i % a == 0 :
#             lista.append(i)
#     print(lista)
# sonic(int(input("숫자를 입력하세요 : ")))
# def sonic(a) :
#     for i in range(1, a+1) :
#         print("%d번 찍혔습니다."%i)
# sonic(100)
# class
# class test :
#     def __init__(self):
#         self.result = 0
#     def sum(self,a) :
#         self.result += a
#         return self.result
# acompany = test()
# acompany.sum(10)
# acompany.sum(20)
# print("b회사의 합계는 ?",acompany.result)
# bcompany = test()
# bcompany.sum(20)
# bcompany.sum(20)
# print("b회사의 합계는 ?",bcompany.result)
# class calculator :
#     def __init__(self):
#         self.result = 0
#     def add(self,a,b):
#         self.result = a + b
#     def sub(self, c , d) :
#         self.result = c - d
#     def mul(self, f , g ):
#         self.result = f * g
#     def div(self, h , l ):
#         self.result = h / l
#         return self.result
# acompany = calculator()
# a = 0
# while a < 10 :
#     a = a + 1
#     acompany.sum(a)
# print(acompany.result)
# class1 = calculator()
# class1.add(10,20)
# print(class1.result)
# class2 = calculator()
# class2.sub(20,10)
# print(class2.result)
# class3 = calculator()
# class3.mul(10,20)
# print(class3.result)
# class3 = calculator()
# class3.div(10,20)
# print(class3.result)
# class rectangle :
#     def __init__(self):
#         self.result = 0
#     def s(self,width,height):
#         self.result = (width + height)* 2
#     def l(self,width2,height2):
#         self.result = width2 * height2
# class rectangle : # 이런식으로도 풀수있다.
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def s(self):
#         self.result = (width + height)* 2
#     def l(self):
#         self.result = width * height
# print("--------------------------------")
# w = int(input("가로의 길이를 입력하세요 : "))
# h = int(input("세로의 길이를 입력하세요 : "))
# class2 = rectangle()
# class2.l(w,h)
# print("--------------------------------")
# class1 = rectangle()
# class1.s(w,h)
# print("사각형의 넓의 : %d"%class2.result)
# print("사각형의 둘레 : %d "%class1.result)
# print("--------------------------------")
class person :
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def display(self) :
        print("이름 : %s \n성별 : %s \n나이 : %s"%(self.name,self.gender,self.age))
w = input("이름 이력 : ")
h = int(input("나이 이력 : "))
z = input("성별(male,female) 입력 : ")
print("=========================")
p1 = person(w,z,h)
p1.display()
print("========================")