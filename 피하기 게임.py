import pygame # pygame 불러오기
import random # random 파일 불러오기
import threading # threading 파일 불러오기

# 색깔
red = (255, 0, 0) # 빨간색 rbg 컬러
green = (0, 255, 0) # 초록색 rbg 컬러
blue = (0, 0, 255) # 파란색 rbg 컬러
black = (0, 0, 0) # 검은색 rbg 컬러
white = (255, 255, 255) # 하양색 rbg 컬러
yellow = (255, 255, 0) # 노랑색 rbg 컬러

pygame.init()  # 게임 초기화
size = [600, 900]  # 화면 크기 변수 만들기
screen = pygame.display.set_mode(size)  # 게임 화면 크기 정하기
clock = pygame.time.Clock()  # 초당 몇번 출력하는지 설정(FPS 설정)
pygame.display.set_caption("피하기 게임") # 대문자로 하기

점수 = 0 # 점수변수를 0으로 설정하기
돌사진 = pygame.image.load('돌2.png') # 돌 이미지 불러오기
캐릭터사진 = pygame.image.load('주인공 캐릭터2.jpg') # 캐릭터 이미지 불러오기
벽돌화면 = pygame.image.load('벽돌화면.jpg') # 배경화면 이미지 불러오기

# 캐릭터 움직이는 것

# 돌이 일정한 위치 아래로 내려가면 사라지게 하는 것

# 돌에 맞으면 게임을 끝나게 하는 것

# 돌이 랜덤한 위치에서 떨어지는 것

# 돌이 랜덤한 위치에 있게하는 변수
돌개수 = [] # 돌의 개체의 정보량 속도를 저장하는 돌 개수 저장 변수
for i in range(10) : # 10번 반복하기
    돌 = pygame.Rect(돌사진.get_rect())  # 이미지로 만든 변수 생성
    돌.left = random.randint(0, size[0]) # 돌의 x의 위치를 0부터  화면 가로크기 까지 랜덤하게 위치하기
    돌.top = -100 # 돌의 y 위치를 -100 위치에 놓기
    돌속도 = random.randint(3, 9) # 돌의 속도를 3부터 9까지 랜덤하게 반복하기
    돌개수.append((돌, 돌속도)) # 돌의 정보들을 돌개수 리스트에 저장하기

# 캐릭터가 정중앙에 있게하는 코드
캐릭터 = pygame.Rect(캐릭터사진.get_rect()) # 캐릭터 이미지로 만든 캐릭터 변수 만들기
캐릭터.left = size[0] // 2 - 캐릭터.width // 2 # 캐릭터의 x의 위치를 화면에 가운데에다가 위치하게 하기
캐릭터.top = size[1] - 캐릭터.height # 캐릭터를 화면 맨아래 위치하게 하기
캐릭터_x = 0 # 캐릭터가 이동하게하는 변수

게임종료 = False # 게임 종료 함수
while not 게임종료 : # # 게임이 종료되엇을대 오류가 걸릴것을 대비해 만든 무한 반복문
    screen.blit(벽돌화면, (0,0)) # 화면을 벽돌화면 위치로 바꾸기
    for event in pygame.event.get(): # 화면안에서일어나는 이벤트를 감지해서 그 행동이 무엇인지 알려주는 반복문
        if event.type == pygame.QUIT : # 만약에 그 이벤트에 종류가 나가는 거라면
            게임종료 = True # 게임종료를 TRUE로 만들기
            pygame.quit() # PYGMAE 나가기

        elif event.type == pygame.KEYDOWN : # 만약 위에 조건이 아니고 행동의 종료키를 누르는 거라면
            if event.key == pygame.K_RIGHT : # 그리고 그 방향키가 오른쪽 방향키라면
                캐릭터_x += 5 # 캐릭터는 x쪽으로 5 이동
            if event.key == pygame.K_LEFT: # 그리고 그 방향키가 오른쪽 방향키라면
                캐릭터_x -= 5 # 캐릭터는 x쪽으로 -5 이동
        elif event.type == pygame.KEYUP : # 만약에 행동키를 누르지 않고 있는 거라면
            if event.key == pygame.K_RIGHT : # 만약에 그 키가 오른쪽 이라면
                캐릭터_x = 0 # 움직이는 x값을 0으로 하기
            if event.key == pygame.K_LEFT : # 만약에 그 키가 왼쪽 이라면
                캐릭터_x = 0 # 움직이는 x값을 0으로 하기

    for (돌, 돌속도) in 돌개수 : # 돌 개수안에있는 정보를 차례로 들고 돌속도에 대입하고 반복
        if 돌.colliderect(캐릭터): # 만약에 돌이 캐릭터와 부딪친다면
            게임종료 = True # 게임종료를 TRUE로 만들기

    for (stone, speed) in 돌개수 : # 돌개수안에 있는 정보를 stone,speed에 차례로 담으면서 반복하기
        stone.top += speed # 돌개수 y값에 speed 더하기
        if stone.top > size[1] : # 만약에 돌개수의 값이 화면보다 커진다면
            돌개수.remove((stone, speed)) # 그 돌을 돌개수에서 제거하기
            stone = pygame.Rect(돌사진.get_rect()) # 돌 이미지를 가진 새로운 stone 변수 만들기
            점수 += 1 # 돌이 없어졌을때 점수 +1
            stone.left = random.randint(0, size[0])  # 새로운 물체의 가로 위치
            stone.top = -100  # 새로운 물체의 세로 위치
            speed = random.randint(3, 9)  # 새로운 물체의 속도
            돌개수.append((stone, speed))  # 새로운 물체를 리스트에 담기

    # 게임 종료 메세지 띄우기
    if 게임종료 : # 만약에 게임 종료가 됬다면
        font = pygame.font.SysFont("malgungothic" , 75) # 맑은 고딕첵의 75크기의 폰드변수 생성
        메세지 = font.render("Gmae over", True, yellow) # Game over을 담은 메세지 함수
        threading.Timer(2.0,screen.blit(메세지,(120,375))).start() # 2초동안 메세지 띄우기

    # 게임 점수 메세지 띄우기
    font1 = pygame.font.SysFont("malgungothic" , 35) # 맑은 고딕첵의 75크기의 폰드변수 생성
    메세지 = font1.render(str(점수)+"점", True, yellow) # Game over을 담은 메세지 함수
    threading.Timer(2.0,screen.blit(메세지,(500,850))).start() # 2초동안 메세지 띄우기

    캐릭터.left = 캐릭터.left + 캐릭터_x #  캐릭터 x의 값에 움직이는 거리를 더하기
    if 캐릭터.left < 0 : # 만약에 캐릭터가 왼쪽 변ㄱ을 나가려고 한다면
        캐릭터.left = 0 # 캐릭터를 왼쪽 끝에 위치하게 하기
    if 캐릭터.left > size[0] - 캐릭터.width: # 만약에 캐릭터가 오른쪽 벽을 넘어가려 한다면
        캐릭터.left = size[0] - 캐릭터.width # 캐릭터를 오른쪽 끝에 위치하게 하기
    for(돌,  돌속도) in 돌개수: # 돌개수 안에 있는 정보를 돌과 돌속도에 담아 차례대로 반복하기
        screen.blit( 돌사진 , 돌 ) # 화면에 돌을 추가하기

    screen.blit( 캐릭터사진, 캐릭터) # 화면에 캐릭터 추가하기

    pygame.display.update() # 화면을 업데이트 하기
    clock.tick(100)  # FPS를 100으로 설정(초당 100번의 화면을 출력)