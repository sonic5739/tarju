# 1.print() 함수
# 정의 : 표준 출력을 하는 함수
# 사용방법 : print("answk)
# 스트림을 강제적으로 flush할지를 지정할때는 flush를 기술합니다.(기본값 : False)
# 2. int() str() fioat() 함수
# 정의 : 숫자로 변환 , 문자로 변환 , 실수로 변환
# 사용방법 :int("문자") , str("숫자") , float("실수")
# 3. 인덱싱이란
# 인덱싱이란 무엇인가를 '가르킨다'는 의미
# 4. 슬라이싱
# 정의 : 슬라이싱은 무엇인가를 '잘라낸다' 라는 의미
# 사용방법 : a[시작번호:끝 번호] 에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.
# 5.replace() 함수
# 정의 : replace는 문자열을 변경하는 함수이다. 문자열 안에서 특정 문자를 새로운 문자로 변경하는 기능을 가지고 있다
# 사용방법 : replace("-" , " ")
# 6.split() 함수
# 정의 : split 자르다 분리 함수
# 사용방법 : split(" ")
# 7. formatting이란
#포맷이란 데이터를 위해 미리 설정되는 레이아웃으로서, 우리말로는 '형식'이라는 용어와 동일하게 쓰인다.
# 8. format() 함수
# 정의 : 형식, 서식, 초기화, 체제, 형 등의 뜻을 가지고 있다.
# 사용방법 : # {}안에 들어갈 데이터를 farmat 함수 안에 넣기
# 9.f-string
# 정의 : f 문자열 포맷팅
# 사용방법 :  f"문자{변수명}
# 10.strip() 함수
# 정의 :공백을제거하는 함수
# 사용방법 : strip( )
# 11.upper
# 정의 : upper 소문자를 대문자로 벼화주는 함수
# 사용방법 : 땡떙.upper()
# 12.lower
# 정의 : lower 대문자를 소문자로 벼화주는 함수
# 사용방법 : 땡떙.lower()
# 13.capitalize() 함수
# 정의 : 첮글자만 대문자로 변환 해주는 함수
# 사용방법 : 땡떙.capitalize()
# 14. endswith() 함수
# 정의 : 끝나는 문자가 맞는지 확인 함수
# 사용방법 : 땡땡. endswith(끝에있는 말)
# 15. startwith() 함수
# 정의 : 시작하는 문자가 맞는지 확인
# 사용방법 : 땡땡. startswith(처음에있는 말)
# 16. rsplit
# 정의 : 오른쪽 공백 제거
# 사용방법 : 땡땡.rsplit()
# 17.lsplit
# 정의 : 왼쪽 공백 제거
# 사용방법 : 땡땡.lsplit()
# 18.변수와 리스트의 차이
# 변수는 하나를 저장한믄 공간
# 리스트는 여러개를 저장하는 공간
# 리스트는 대괄호
# 19.append() insert()
# 정의 : 리스트에 변수를 추가하는 함수,리스트 가운데에 변수를 추가하는 함수
# 사용방법 : 떙떙.append(),떙떙.insert( 숫자 , 떙떙 )
# 20. del
# 정의 : 삭제
# 사용방법 : del 떙떙[숫자]
# min() max() sum() len() 함수
# 정의 : 최소 , 최고 , 리스트내 숫자를 다 합침 , 리스트내 숫자의 수
# 사용방법 : (min()) , (max()) (sum()) (len())
# 데이터를 저장하는방법 4가지의 차이와 사용방법
# 변수 = 데이터를 하나만 저장 sonic = "gh1"
# 리스트 = 데이터 여러개를 저장 ,대괄호 사용 sonic = [값1 ,  값2 , 값3 ...]
# 튜틀 = 리스트와 거의 유사 하지만 한번 생성되면 값을 변경할수 없음,소괄호 사용 튜플명 = (값1,값2,값3...)
# 딕션어리 =Key와 Value를 한 쌍으로 갖는 자료형 이다 => 사전 , {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# join 함수
# 정의 : 문자열 합치다
# 사용방법 : " ".join(떙땡)
# \n \t
# 정의 : 줄바꿈 제어문자  ,  들여쓰기 제어문자
# 사용방법 : print(\n,떙땡)
# sort reverse
# 정의 : 오름차순 정리 , 내림차순
# 사용방법 : sort.땡땡() , sort.떙땡(reverse=True)
# 튜플을 리스트로 바꾸는 방법
# print( list( 땡땡 ) )
# 리스트를 튜플로 바꾸는 방법
# print(tuple( 땡땡 )
# paking
# 정의 : 묶음 예) 리스트 , 튜플 , 딕션어리
# unpaking
# 정의 : 묶음x : 데이터 한개 예) 변수
# 사용방법
# temp = ('apple','banana','cake')
# a , b , c = temp
# print( a , b , c )
# 딕셔너리 활용
# 1.딕셔너리 리스트 추가하는 방법 : 딕셔너리명 = { " 키 " : 리스트  ,  "키2" : 리스트2 , "리스트2 ,"키3" : 리스트3 }
# 2.딕셔너리의 키 만 출력하는 방법 : list(땡땡.keys() )
# 3.딕셔너리의 값 만 출력하는 방법 : list(땡땡.values() )
# 4.두개의 딕셔너리를 합치는 방법 : 딕겨너리명1.update( 딕셔너리명2) : 딕셔너리명1에 딕셔너리명2 추가
# 5.[키] 튜틀과 [값] 튜틀 을 딕셔너리 변환하는 과정# dict( zip( 투틀1 , 투틀2) )
# 6.[키] 리스트와 [값] 리스트 을 딕션어리로 변환하는 방법 : dict( zip( 값1 , 값2) )
# (1)IF 활용
# 정의 : 영어 단어로서 "만약에"란 의미. 여러 프로그래밍 언어에서 조건문이나 조건식을 표현하는 데 if를 쓴다.
# 사용방법 :
      # if 논리 :
      #     참 [ 코드 ]
      # if 논리2
      #     참2 [코드2]
      # if 논리3 :
      #     참3 [ 코드3 ]
# (2)IF 변수 in 리스트 명
# 정의 : 그 변수가 리스트에 포함되어 있으면
# 사용 방법 : if 입력과일 in 과일
# input 함수
# 정의 : 키보드로 입력받는 함수
# 사용방법 : 땡땡 = input( " 땡 : ")
# 배수구하는 방법
# 배수
# 값 % 수 == 0 : 나머지가 0이면 그값 은 그의 수의 배수
# 홀수 짝수 수하는 방법
# 홀수/짝수 : 값%2 == 0
# 짝수 //  값%2 == 1 홀