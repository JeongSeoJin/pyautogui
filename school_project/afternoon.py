import schedule
import datetime
import pyautogui
import time
import sys
import pyperclip
import os
import random
import threading

# 좌표 객체 얻기 
position = pyautogui.position()

# 화면 전체 크기 확인하기
print(pyautogui.size())

# x, y 좌표
print(position.x)
print(position.y)

# 마우스 이동 (x 좌표, y 좌표)
# 마우스 이동 (x 좌표, y 좌표 2초간)
# pyautogui.moveTo(100, 100, 2)  

# # 마우스 이동 ( 현재위치에서 )
# pyautogui.moveRel(200, 300, 2)

# # 마우스 클릭
# pyautogui.click()

start = "조례, 통합사회, 온라인 독서실 줌 링크(고윤호t): https://us04web.zoom.us/j/6650751611?pwd=eVJPQStYWkxCbUs4dmFnWkU2VVFYQT09"
koreanshj = """국어(김효수t): Zoom 회의 참가
https://us05web.zoom.us/j/3607303185?pwd=bDY2WUZ6dkRITW9ZZGQzcEJESDN5dz09

회의 ID: 360 730 3185
암호: Cdecc6""" #(성현진)https://us02web.zoom.us/j/81478779105?pwd=NmFraEt1UkJSKzQvbmV6Y1hJMVhMQT09"
korean2gjg = "국어(구진교t): https://zoom.us/j/3643393628?pwd=aUFncFl1azZFTnByeEo0YTZJbHRKUT09"
mathymg = "수학(윤명기t): https://us04web.zoom.us/j/7021657995?pwd=UGs5T0RLVDcydi8ydmk5ZVlZd0FIUT09"
societygyh = "통합사회(고윤호t): https://us04web.zoom.us/j/6650751611?pwd=eVJPQStYWkxCbUs4dmFnWkU2VVFYQT09"
societypsm = "통합사회(박상민t): https://us04web.zoom.us/j/9019173369?pwd=RUJuZjArN1Y3T3VLQUN5cXBjMzJIQT09"
sciencejgm = "통합과학(정기문t): https://us04web.zoom.us/j/9753836691?pwd=R1RJZ1B3bnJ6RkllRmRzdFYwaXNNUT09"
sciencejyn = """온라인 기간 통합과학 정유니T ZOOM 링크 입니다.
수업방식은 1학기 온라인기간과 동일하게 진행합니다. 늦지않게 접속하세요.

주제: 통합과학(정유니T) ZOOM
Zoom 회의 참가
https://us04web.zoom.us/j/73537149833?pwd=UEpjdFd4aldrVlVld0pDYkJNUno2Zz09

회의 ID: 735 3714 9833
암호: science"""

experienceshj = "과학탐구실험(서환주t): https://us02web.zoom.us/j/86511917982?pwd=ZURtWTZJNFE2SnJvTVhJcXFEbjZzQT09"
englichldh = "영어(이도현t): https://us04web.zoom.us/j/8241233916?pwd=OUFsZWRMTXZXZTFHMFR2di9VQ3g2UT09"
englishchg = """
영어(최해경t):
1. 1학년 영어(최해경) 수업은 수업이 시작되면 35분간 EBS 온라인 클래스 강의 듣기
2. 수업 종료 10분전 줌으로 들어와 수업에 관한 질문 및 발표하기
  (반드시 비디오 켜고 얼굴 보여줘야 합니다)
3. 줌 링크
https://us04web.zoom.us/j/9807451785?pwd=ZkdVV3ZXZnBJM256T0FpSitBc052Zz09
"""
historylgj = """한국사 근현대사(이광종t)
1. 35분 이내 촬영 수업 수강 : EBS온라인 클래스
2. 10분 가량 : 줌에 접속하여 실시간 수업 진행.
https://us04web.zoom.us/j/73603445786?pwd=MnBpQUJVRHZXVXRoNTYxbk5ZSU5uUT09
"""
historymcb = "한국사 전근대사(문창배t): https://zoom.us/j/8358880420?pwd=RWZmejNnYlVOK0Q4T1ZWU0ZGdzlSdz09"
exerciselhc = "체육(류호천t): https://us04web.zoom.us/j/9660123898?pwd=enRaS3FtdVl4d05nVDRzQ2lvT0kzUT09 "
musickgy = "음악(김지영t): 회의 ID: 5375005148 비밀번호: 1"
futurelsj = "진로(이수정t):https://zoom.us/j/4552595865?pwd=bExJb3dsT2Nza0dFd1VvSnBVUHcwZz09"
artksj = "한문(이교찬t) : https://us04web.zoom.us/j/8589258919?pwd=Y080aFlxN1NvbzFIVGlwSGh2N2tFdz09  기술가정(김순주t): https://us02web.zoom.us/j/89774835212?pwd=bkd1M3QrUzE0WlY3OE0ybThEUTh0dz09"
# pyautogui.moveTo(500, 800)
artcs = """[양일 박상민t (일사)] [오전 9:07] SeongDeok Choi이(가) 예약된 Zoom 회의에 귀하를 초대합니다.

주제: 고1미술
시간: 2021년 8월 17일  10:00 오전 오사카, 삿포로, 도쿄

Zoom 회의 참가
https://us02web.zoom.us/j/82991214084?pwd=OW1EeU5RN1NkYlVOUjBmblZldndsZz09

회의 ID: 829 9121 4084
암호: 1234"""


mon = [historylgj, sciencejyn, artksj, mathymg]
tus = [societypsm, koreanshj, artksj, englishchg]
wed = [mathymg, historylgj, artcs, englichldh]
thu = [artcs, experienceshj, exerciselhc, societypsm]
fri = [artcs]

now = datetime.datetime.now()

days = ["mon", "tus", "wed", "thu", "fri", "sat", "sun"]

i = 0

def check_time():
    global mon, tus, wed, thu, fri
    global days, a

    def send_msg():
        global i
        now1 = datetime.datetime.now().weekday()
        today = days[now1]
        print(today)

        pyautogui.moveTo(2480, 1720, 0.5)
        pyautogui.doubleClick()
        time.sleep(6)

        pyautogui.moveTo(2100, -70, 0.5)
        pyautogui.doubleClick()
        time.sleep(1.5)

        pyautogui.moveTo(2450, 385, 0.5)
        pyautogui.doubleClick()

        if today == "mon":
            pyperclip.copy(mon[i]) 

        if today == "tus":
            pyperclip.copy(tus[i]) 

        if today == "wed":
            pyperclip.copy(wed[i])

        if today == "thu":
            pyperclip.copy(thu[i]) 

        if today == "fri":
            pyperclip.copy(fri[i]) 
        i += 1

        pyautogui.hotkey('ctrl', 'v') 
        pyautogui.keyDown('enter')

        threading.Timer(3300, send_msg).start()

        # schedule.every().day.at("02:18").do(send_msg)
    
    # if now.hour == 12 and now.minute ==45:
    if now.hour == 13 and now.minute ==5:
        send_msg()
        
        # schedule.every().day.at("11:40").do(send_msg)

    # send_msg()

if __name__ == '__main__':
    check_time()
