# list = [1,2,3,4,56]
# a= list.pop()
# print(a)
# print(list)
# a = 2
# print("성공했을때 실행문") if a >10 else print("실패했을때 실행문") # 조건문을 한줄에 모아놌는 방법
# def out(a) :
#     for  i in range(0,len(a)) :
#         print(a[i])
# out([1,2,3,4,5,6])
# out([4,5,6,7,2])
# out([1,2,3,4,5,54])
# class sonic :
#     def output1(self, la):
#         for i in range(0,len(la)) :
#             print(la[i])
#     def output2(self,la):
#         for i in range(1,len(la)) :
#             print(la[i])
#     def output3(self,la):
#         for i in range(2,len(la)) :
#             print(la[i])
# o1 = sonic()
# o1.output1([1,2,3])
# o1.output2([4,5,6])
# o1.output3([7,8,9])
import os
#
# f = open("test.txt",'a')
# f.write(  "\nsonic")
# f.close()
# a = open("tast5.txt",'a',encoding='UTF-8')
# for i in range(101,202) :
#     a.write("%d번째 줄입니다.\n"%i)
# a.close()
# with open("tast5.txt",'w',encoding="UTF-8") as t :
#     for i in range(1,101) :
#         t.write("%d번째 고객입니다.\n"%i)
# t = open("tast5.txt",'r',encoding="UTF-8")
# data = t.readlines()
# for i in data :
#     print(i,end='')
# t.close()
#!/usr/bin/env python3
# Anchor extraction from HTML document
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     print(soup)
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))
# from urllib.request import urlopen
#
# from bs4 import BeautifulSoup
#
# print(" # 오늘의 날씨")
# with urlopen('https://weather.naver.com/today/09140104') as response :
#     soup = BeautifulSoup(response,'html.parser')
#     temps = soup.find("strong","current")
#     cast = soup.find("span","weather")
#     print('--> 서울 기온 : ',temps.get_text())
#     print('--> 서울 날씨 : ', cast.get_text())
# import time
# print("현재 시작은 %d:%d:%d: 입니다."%(time.localtime().tm_hour-12,time.localtime().tm_min,time.localtime().tm_sec))
# print("타임슬립 시작")
# time.sleep(1)
# print("타임슬립 끝")
# import random
# print(random.randint(1,10))
# print(random.random())
# a = random.randint(1,10)
# b = random.randint(1,101)
# print("%d + %d = %d"%(a,b,a+b))
import webbrowser
url = 'https://www.naver.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'