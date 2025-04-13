'''
 1. map함수
 - 각 항목에 동일한 함수를 적용하여 새로운 리스트를 만들때 사용
 - 기본구조
    map(적용할_함수, 반복 가능한 객체)
    객체로 값을 만들어 주기 때문에 변환하는 형태를 map 함수 밖에 지정해줘야힘
  
'''

 #number를 문자로 바꿔주고 싶어
 # ['1', '2', '3', '4', '5']
  
numbers = [1, 2, 3, 4, 5]
str_numbers =list(map(str, numbers))
print(str_numbers)
 
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)
 
 