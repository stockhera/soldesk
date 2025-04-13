# module 파일을 끌어와서 사용해보기

'''
1. import module
- import  모듈이름 (확장자명 .py가 없는 파일이름)
- from 모듈이름 import 모듈함수, 변수, 클래스
'''

import _module #모듈을 전체를 import를 하면, 
 
var_add = _module.add(10,20) #모듈명을 불러와야 함
var_lang = _module.DEV_LANG
print(var_add, var_lang) #300 100 30이 나오게 됨. 모듈을 import하면 모듈이 다 실행이 됨. 우리가 원하는 것은 30만 조회되는 것.

# 이렇게 사용하는 것을 추천
from _module import add, sub, DEV_LANG, CEO_NAME
print(add(200,100), DEV_LANG)

print(f"우리회사 대표님 성함은 {CEO_NAME}입니다.")
print(f"우리회사 대표님 성함은 홍길동 입니다.") # 이렇게 작성하면 절대 안됨