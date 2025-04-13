'''
  module이란...
  함수나 변수 또는 클래스를 모아놓은 파이썬 파일...

'''
def add(first, second):
    return first + second

def sub(first, second):
    return first - second

PI = 3.14
DEV_LANG = 'PYTHON'

class FourCalc():
    def class_mul(self, first, second):
        return first * second

# __name__변수는 
# 1. 현재페이지에서 실행을 하면 "__main__"
# 2. 다른페이지에서 import하면 "_module" (화일명)

#페이지마다 공통적으로 사용하는 데이터 값은 하나에 다 작성
COMPANY_ADDR = "서울 강남구"
COMPANY_TELENO = "02-1111-2222"
CEO_NAME= "STOCKHERA"

if __name__ == "__main__": # 이 모듈은 현재 페이지에서만 실행하고, 다른 페이지에서는 실행하지 않는다
    print('name',__name__)
    print(add(100,200))
    print(sub(200,100))