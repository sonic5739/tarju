# print("Hello python")
# a = 10
# print(a)
# a = 10+a
# print(a)
# a = 10
# b = 10.5
# print(type(a))
# print(type(b))
# a = 3
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# a = "hello python1"
# b = 'hello python2'
# c = '''
# hello
# pytHon
# '''
# print(c)
# print( a + b + c )
# a = "hello's"
# print(a)
# a = "hello \n ppp"
# print(a)
# a = "python"
# b = "hello"
# print( a * 2 + b )
# a = "hello"
# print(a[0:5]) # 아무것도 넣지 않으면 끝까지 간다
# print(a[:5])
# a = "python hello"
# print(a[::2]) # 마지막은 항상 건너뛰는 간격이다. 만약 1 이라면 달라지는 것이 없다.
# b = "python"
# a = "hello %s" % b # b 는 %s 자리에 들어간다. # 만약 %s 자리에 d가 들어가면 문자만 입력받을수있다 하지만 s가 들어가면 숫자와 문자만 들어간다.
# print(a)
# b = input("좋아하는 동물를 고르시오")
# a = "hello %s" % b
# print(a)
# a = "elephent"
# print(a.count('e')) # count함수는 내가 세고 싶은 문자의 개수를 위에있는 문자열에서 몇게있는지 세주는 것이다.
# a = "elephent"
# b = a.find('p') # find함수는 위에 문자열에서 내가 입력한 문자가 몇번째에 있는지 찾아주는 것이다.
# print(b)
# a = "hi"
# b = a.upper() # upper함수는 a 문자열을 대문자로 바뀌주는 함수이다.
# print(b)
# c = "HI"
# d = c.lower() # lower함수는 a 문자열을 소문자로 바뀌주는 함수이다.
# print(d)
# a = " hi "
# b = a.strip() # 만약 " hi " 처럼 양쪽에 공백이있을때 strip를 쓰면 양쪽 공백이 사라진다.
# print(b)
# a = "hello python"
# print(a.replace("python"," C++ ")) # replace함수는 문자열에서 어떤 문자를 대신하여 딴 문자를 넣는 것이다.
# a = "I like python"
# print(a.split()) # split함수는 문자열을 뛰어쓰기 기준으로 짤라서 리스트를 만들어준다.
# a = [ 10 , 20 , 30 ] # 리스트는 여러가지 변수를 한 변수로 보은 것이다.
# print(type(a))
# print(a)
# print(a[2])
# print(a[1:3]) #  인덱싱과 슬라이싱은 다 똑같이 리스트명[],리스트명[ : ] 으로 쓰면 된다
# a = [ 1 , 2 , 3 , 4 , 5 ]
# b = [ 10 , 20 , 30 , 40 , 50 ]
# print(a+b)
# a = [1,2,["김돌쇠","김갑돌"]]
# print(a[2][0])# 리스트 안에있는 리스트의 값을 출력하고싶으면 리스트명[][] 을 사용한다
# b = [ 1 , 3 , 5 , 7 , 9 , 10 ]
# b[3] = 8
# print(b)
# print("제 이름은 %s 입니다.나이는 %d" % ("김태주",15)) # 포매팅 할 것이 두개 일때는 두개를 괄호로 묶고 가운데에 쉼표를 찍는다.
# a = [ 10 , 20 , 40 , 50 , 60 ]
# b = a.remove(30) # 여기에 del 리스트명[숫자] 으로 쓸수있다. 또한 리스트명[그 값 : 다음 값 ] = []로 쓸수 있다
# print(a)
# a[2:3] = []
# print(a)
# a.insert(2, 30 ) # insert는 내 가 넣고 싶은 위치에 숫자를 넣을수 있고 insert를 쓸때 괄호에 내가 넣고 싶은 자리를 쓰고 콤마를 쓴뒤에 내 넣고싶은 숫자를 넣는다.
# a.append(70) # append는 무조건 리스트 가장 맨 끝자리에 숫자가 들어간다.
# print(a)
