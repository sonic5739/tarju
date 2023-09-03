# 1. pygame 설치
import pygame
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_LEFT , K_RIGHT , K_DOWN
# 종료 , 작각 , 키 눌렀을때 , 위방향키 , 왼쪽방향키 , 오른쪽키 , 왼쪽키를 눌렀을 때
import random # 랜덤 파일 불러오기
import sys # 시스템 파일 불러오기

# 2. 게임에 필요한 기본 설정
pygame.init() # 파이게임 초기값
화면 = pygame.display.set_mode( (1000,1000) ) # 화면 구성
프레임 = pygame.time.Clock() # 프레임에 파이게임 시간 설정
# FRAME Per Second : FPS : 초당 프레임[정지사진]수
# 3. 함수 만들기
음식 = [ ] # 여러개 음식을 저장할 리스트
뱀 = [ ] # 여러개 뱀 꼬리를 저장할 리스트
( 가로 , 세로 ) = (50,50) # 가로길이 세로길이 튜플선언
배경 = pygame.image.load('정글사진.jpg') # 배경 사진 넣기
# 3. 함수 만들기
# 1)음식함수
def makefood() : # 임이의 장소에 음식을 배치하는 함수
    while True : # 무한반복 하기
        위치 = ( random.randint( 0 , 가로-1 ), random.randint( 0 , 세로-1 )) # 난수 생성
# 가로 (0부터 19까지 난수 생성) , 세로 (0부터 19까지 난수 생성)
        if 위치 in 음식 or 위치 in 뱀 : # 해당위치에 뱀이나 음식이있으면
            continue # 계속
        else:
            음식.append(위치)
            break  # 반복문 끄기
# 2) 음식 이동 함수 : 뱀이3 음식을 먹었을 때
def foodmove(위치) : # 인수가 있는 함수 선언
    sonic = 음식.index(위치) # 해당 위치에 음식이 존재 하면
    del 음식[sonic] # 찾은 음식 삭제
    makefood() # 새로운 음식 생성
# 3) 그리기 함수
def draw( 점수판 , 게임종료메세지 )  : # 화면 그리기 함수
# (1) 음식그리기
    for food in 음식 :
        pygame.draw.ellipse( 화면 , (0,255,0) , Rect( food[0]*20 ,food[1]*20 , 20 , 20 ) )
    # 타원그리기( 화면이름 , (칼라[RBG]) ,  # 타원( x축위치     y축위치 , 가로크기 , 세로크기 )
# 뱀 그리기
    for body in 뱀 :  # 뱀 리스트에 존재하는 변수 만큼 그리기
        pygame.draw.rect( 화면 , (0,255,255) , Rect(body[0]*20, body[1]*20 , 20 , 20 ) )
          # 사각형그리기( 화면이름 , (칼라[RBG]) ,  # 사각형( x축위치     y축위치 , 가로크기 , 세로크기 )

    # 점수 그리기
    if 점수판 != None : # 점수에 내용이 있으면
        화면.blit( 점수판 , (10 , 10) ) # x좌표 y 좌표에 표기
    # 종료메세지 그리기
    if 게임종료메세지 != None : # 점수에 내용이 있으면
        화면.blit( 게임종료메세지 , (300 , 500) ) # x좌표 y 좌표에 표기

    pygame.display.update() # 화면 업데이트
# 4. 게임실행
my글꼴 = pygame.font.SysFont( "malgungothic" , 30 ) # 글꼴 글자크기

키 = K_DOWN # 아래키
게임종료 = False # 게임종료 스위치
뱀.append( ( int(가로/2) , int(세로/2) ) ) # 화면에 가운데부터 뱀꼬리 추가
점수 = 0
속도 = 0
for i in range(30) :
    makefood()

while True : # 계속 반벅하기

    화면.blit( 배경, (0, 0 ))  # bilt함수로 배경 넣기

    # 키보드 동작하기'
    for 동작 in pygame.event.get():  # 파이게임에서 이벤트[동작]이 있을 경우
        if 동작.type == QUIT:  # 이벤트가 종료이면
            pygame.quit()  # 파이게임 종료
            sys.exit()  # 시스템[모든코드] 종료
        elif 동작.type == KEYDOWN:  # 키를 눌럿을때
                키 = 동작.key

    if not 게임종료 : # 게임종료가 아니면
        if 키 == K_LEFT : # 왼쪽 키를 눌렀을 때
            머리 = ( 뱀[0][0] - 1 , 뱀[0][1] ) # x축[-] 왼쪽으로 이동
        elif 키 == K_RIGHT : # 오른쪽 키를 눌렀을대
            머리 = (뱀[0][0] + 1 , 뱀[0][1]) # x축 [+] 오른쪽으로 이동
        elif 키 == K_UP : # 위쪽 키를 눌럿을때
            머리 = (뱀[0][0] , 뱀[0][1] -1 ) # y축 [-] 위쪽으로 이동
        elif 키 == K_DOWN : # 아래쪽 키를 눌렀을때
            머리 = (뱀[0][0] , 뱀[0][1] +1 ) # y축 [+] 아래족으로 이동

        if 점수 > 10 :
            속도 += 5

        # 벽 몸에 다앟을때 혹은 화면 밖으로 나갔을때 게임종료
        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= 세로 or 머리[1] < 0 or 머리[1] >= 가로 :
            게임종료메세지 = my글꼴.render("게임 종료 [ 획득점수는 : " + str(점수) + " ]" , True, (255, 255, 255))
            draw( 점수판 , 게임종료메세지 )
            break

        # 뱀 한마리  추가
        뱀.insert( 0 , 머리 )

        # 음식을 먹었을때 꼬리 추가 아니면 추가x
        if 머리 in 음식 : # 만약 머리가 음식에 닿았으때
            foodmove( 머리 ) # 새로운 음식 추가
            점수 += 1 # 점수1점 추가
        else: # 음식을 못먹었으면
            뱀.pop() # 리스트내 가장 뒤에있는 항목 제거
        게임종료메세지 = my글꼴.render("" + str(점수), True, (255,255,255) )
        점수판 = my글꼴.render("현재 먹은 횟수 : " + str( 점수 ) , True ,(255,255,0) )
    draw( 점수판 , 게임종료메세지 )
    프레임.tick(5)
