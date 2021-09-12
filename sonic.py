# 파일 사용하기 = 파일 입출력
# HELLO.TXT 파일을 w모드 (write)로 열기
import pickle

file = open('hello.txt','w')
file.write('Hello World')
file.close()

file2 = open('hello.txt','r')
s = file2.read()
print(s)
file2.close()
# with as 를 사용하여 열고 닫기 한번에 하기
with open('python.txt','w') as file :
    file.write('Python')
with open('python.txt','r') as file :
    s = file.read()
    print(s)
fruits = ['apple','orange','grape']
with open('fruits.txt','w') as f :
    f.writelines(fruits)
with open('fruits.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
name = 'James'
age = 30
fruits = ['apple','orange','grape']
scores = {'korean' : 90,'math' : 80,'english' : 70}
with open('info.p','wb') as file :
    pickle.dump(name,file)
    pickle.dump(age, file)
    pickle.dump(fruits, file)
    pickle.dump(scores, file)
with open('info.p','rb') as file :
    name1 = pickle.load(file)
    age1 = pickle.load(file)
    fruits1 = pickle.load(file)
    scores1 = pickle.load(file)
    print(name1)
    print(age1)
    print(fruits1)
    print(scores1)
words = ['anonymously\n',
'compatibility\n',
'dashboard\n',
'experience\n',
'photography\n',
'spotlight\n',
'warehouse']

with open('words.txt', 'w') as f:
   f.writelines(words)

with open('words.txt', 'r') as f:
   lst = f.readlines()
   count = 0
   for w in lst:
       if len(w.replace('\n', '')) <= 10:
           count += 1
   print(count)
with open('words.txt', 'w') as f:
   f.write('Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.')

with open('words.txt', 'r') as f:
   s = f.read()
   l = s.split(' ')
   for word in l:
       if 'c' in word:
           print(word)

이름 = 'James'
나이 = 30
신용도 = 5
계좌에보유중인금액 = 100000
현재대출중인금액 = 50000000
통장번호 = 1234567890
비밀번호 = 1234
while True:
    print('[메가은행 ATM 프로그램]')
    print('사용하실 서비스를 선택하세요')
    print('1. 입금')
    print('2. 출금')
    print('3. 통장조회')
    print('4. 계좌 만들기')
    print('0. 종료')
    menu = int(input('메뉴 번호를 입력하세요 >> '))
    if menu == 1:
        int(input('이름을 입력하세요 >> '))
        int(input(' 계자 번호를 입력하세요>>'))
        if int(input('입금할 금액을 입력 하세요 >>')) < 0 :
            print('이 금액은 입금 하실수 없습니다')
        else :
            print('해당 계좌로 돈을 입금 하였습니다')
            print('입금을 완료했습니다')
    elif menu == 2:
        int(input('이름을 입력하세요 >> '))
        int(input('계자번호를 입력하세요 >> '))
        if int(input('출금할 금액을 입력하세요 입력하세요 >> ')) < 0 :
            print('이 금액은 출금하실수 없습니다')
        elif int(input('출금할 금액을 입력하세요 입력하세요 >> ')) > 100000 :
            print('이 금액은 출금하실수 없습니다')
        else :
            print('해당 계좌로 출금 하였습니다')
            print('출금이 완료 되었습니다')
    elif menu == 3:
        int(input('이름을 입력하세요 >> '))
        int(input('계자번호를 입력하세요 >> '))
