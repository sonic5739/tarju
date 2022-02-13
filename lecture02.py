# a = [1,3,5,7,9,10]
# a[ 1 : 5 ] = 2,3,4,5
# print(a)
# a.remove(3)
# del a[1]
# print(a)
# b = ["김돌쇠","김갑돌","김갑순","김철수"]
# b.append("이철수")
# b.insert( 1 , "김갑수" )
# print(b)
# b.sort(reverse=True) # 오름차순에서 괄호안에 reverse= True 를 넣으면 내림차순으로 정리한다
# b.sort() # 이 함수는 오름착순을 하는 함수이다
# b.reverse() # 리스트의 순서를 거꾸로 뒤집어 주는 함수이다.
# print(b.index("김갑돌")) # 무슨무슨 문자가 어디있는지 알려주는 함수이다.
# print(b.pop()) # 리스트의 마지막 것을 빼어 온다
# c = b.count("김철수") # 리스트에 내가 쓴 값이 몇개있는지 확인하는 것이다.
# print(c)
##### 튜플
# t = ("hello","python","may")
# print(t[0:2])
# print(t[2])
# t = ("s",'u',"n")
# t2 = ('d',"a","y")
# print(t+t2) # 튜플도 마찬가지로 더하기가 가능하다.
# print(t*2+t2*6) # 곱하기도 가능하다
##### 딕셔너리
# d = { "이름" : "김태주" , "나이" : 15 , "성별" : "남" }
# print(d["이름"])
# print(d["나이"])
# print(d["성별"]) # 딕셔너리 안에있는 문자를 빼내려면 그 value의 key를 대 괄호안에 쓴다.
# print(d.get("나이")) # 딕셔너리를 이런식으로도 호출할수있다.
# d["별명"] = "김타주"
# del d['이름']
# d["이름"] = "김태자"
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
##### 집합
# z = { 1 , 2 , 3 }
# print(z) # 집합에서는 중복이 되지 않는다.  z = { 1 , 1 , 2 , 3 } 이런 집합을 출력해도 {1,2,3} 이라고 출력된다.# print(z[2]) 집합에서는 순서가 없어 인댁싱 슬라이싱을 할수없다.
# 집합 선언 방법
# s = { 1 , 2 , 3 , 4 , 5} # 변수명 = { }
# s = { 1 , 2 , 3 }
# s2 = { 2, 4 , 6 , 8 }
# print( s & s2 ) # 교집함
# print( s | s2 ) # 합집합
# print( s - s2) # 차집합
# print( s2 - s ) # 차집합
# s.add(6) # 추가
# s.remove(6) # 삭제
# print(s)
##### 불
# 조건문 반복문은 조건식에 맞을 경우에만 실행을 한다.
# money = int(input("돈이 얼마나 있으십니까 ?"))
# if money >= 10000 : #
#     print("택시를 타겠다.")
# else :
#     print("걸어가겠다.")
# a = int(input("돈이 얼마나 있으십니까 ?"))
# if a >= 5000 and a < 10000 :
#     print(" 버스를 탑니다.")
# if a >= 10000 :
#     print("택시를 탑니다")
# else :
#     print("걸어갑니다")
# money = int(input("돈이 얼마나 있으십니까 ?"))
# xory = input("다리가 아픈가요?(아프면 yes 않아프면 x)")
# if money >= 10000 and xory == 'yes' : # 아무일도 일어나지 않게 하려면 pass를 쓴다.
#     print("택시를 타세요  ")
# else :
#     print("걸어가세요")
# a = 300
# if a > 400 :
#     pass
# else :
#     print("400이상입니다.")
# m = int(input("돈이 얼마나 있습니까 ?"))
# if m >= 10000 :
#     print("택시를 타시오")
# elif m < 10000 and m >= 2000 : # 2번째 부터는 elif를 쓰면 좀더 좋다
#     print("버스를 타세요")
# elif m < 2000 and m >= 1000 :
#     print("킥보드를 타세요")
# else :
#     print("걸어가세요")
# while
# a = 0
# while a < 100 :
#     a = a + 1
#     print("나무가 %d번 찍혔습니다." % a)
# for i in range(int(input("몇번 찍혔습니까?"))) :
#     print("나무가 %d번 찍혔습니다" % i)
#     if i > 10 :
#         print("나무가 쓰러졌습니다.")
# l = int(input("몇개 입력하실겁니까?"))
# i = []
# a = 0
# while a < l :
#     random = int(input("아무수나 입력하세요"))
#     i.append(random)
#     a = a + 1
# print(i)