'''
1.내장함수 (Built-in Function)
- 파이썬이 기본적으로 제공하는 함수
- 별도의 iumport없이 바로 사용 가능
ex. print(), len(), input(), range()

2.모듈 (Module)
- 파이썬은 기본적으로 많은 기능을 모듈로 제공
- 필요할 때 import를 통해 불러와서 사용
ex. datetime, os, random 

3. 내장함수와 모듈의 차이 
- 파이썬 = > 필요한 것만 가져다 쓴다
- import를 통해 모듈을 불러오면 함수이름이 같은 충돌을 방지할 수 잇다.
  import cal_1
  import cal_2
  cal_1.add()
  cal_2.add()
'''

# 1. os 모듈 (화일 경로를 가져오는 모듈)
import os

def os_module():
    print(__file__) # c:/python_930/A50_모듈/10_about_module.py (정확하지 않을 수도)
    now_path = os.path.abspath(__file__) # 절대경로를 가져오는 가장 확실한 방법
    now_dir_name = os.path.dirname(now_path) #지금 파일의 디렉토리명
    print(now_path)
    print(now_dir_name) # c:/python_930/A50_모듈
    print(now_gwd = os.getcwd())
    
# 2. random
import random

def random_module():
    var_ran = random.randint(1,10) #1부터 10까지 수중에서 랜덤으로 숫자를 불러온다
    if var_ran < 5:
        print('당첨')
    else: 
        print('꽝')

    var_list = [1, 2, 3, 4, 5]
    var_list_ran = random.choice(var_list) #var_list에서 랜덤선택
    print(var_list_ran)

    var_ran_float = random.random() #0~1 상의 소숫점을 랜덤으로 생성
    if var_ran_float < 0.5:
        print(var_ran_float, "당첨")
    else:
        print(var_ran_float, "꽝")

#3. datetime

from datetime import datetime 
from datetime import timedelta

def datetime_module():
    #현재시간
    now = datetime.now()
    #날짜 → 문자 : string format time = strftime
    string_datetime= now.strftime("%Y-%m-%d %H:%M:%S") #2025-04-12 11:55:14
    print("포맷된 날짜 시간:", string_datetime)

    string_date= now.strftime("%Y-%m-%d")
    print("포맷된 날짜:" , string_date)
    # %Y: 연도 4자리
    # %y: 연도 2자리
    # %M: 시간 분 표기
    # %m: 월 표기
    # %D: mm/dd/yy


    # 문자열 → 날짜 string parse time 
    date_string = '2025-12-25 11:57:03'
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(parsed_date)
    
# 날짜 간의 차이 계산하는 모듈
from datetime import timedelta

def timedelta_module():
    now = datetime.now()
    future_date = now + timedelta(days=10)
    print("10일 후의 일자: ",future_date)

    # 두 날짜의 차이 계산

    date1 = datetime(2025,12,25)
    date2 = datetime(2025, 10, 5)
    differ = date1 - date2
    print(differ) #81days
    print("date1 →", date1, "date2 →", date2)

    # 특정 날짜의 요일 확인
    weekday = date1.weekday()
    print(weekday) #3은 목요일 / 0: 월요일, 1: 화요일, 2: 수요일, 3: 목요일....

    if date1 > date2:
        print(f"{date1}은 {date2}보다 이후 입니다.")
    else:
        print(f"{date1}은 {date2}보다 이전 입니다.")