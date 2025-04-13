'''
1.내장함수 (Built-in Function)
- 파이썬이 기본적으로 제공하는 함수
- 별도의 iumport없이 바로 사용 가능
ex. print(), len(), input(), range()
'''

#1. abs(): 절대값
def in_abs():
    print(abs(-3))
    print(abs(3))

#2. type(var): var의 자료형 type을 출력
print(type('str')) #str
print(type([])) #list
var_a = {} #dict
print(type(var_a))

#3. dir() : 객체가 가진 변수나 함수를 보여주는 함수
def in_dir():
    print(dir(dict))
# print(dir(list)) #'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#4. 형
# 변화
def in_change_type():
    #int()형
    print(int(1.2))
    #str()
    print('1'+str(2))
    #list()
    a = list('python')
    print(a, type(a))
    #tuple()
    b = tuple(a)
    print(b)
  
#5. all(x) : [and], 반복가능한 데이터 (iterable변수) x 중에 모두 참여면 True, 거짓이 하나라도 있으면 False
# - 반복 가능한 데이터란 for 문에서 사용할 수 있는 자료형
# - 리스트, 튜플, 문자열, 딕셔너리, 집합 등 

def in_all():
    args = [1, 2, 3, 0] # 숫자 중의 0은 false
    result = True
    for arg in args:
        if  not arg:
            result = False
            
    print(result) 

def false_iterable():
    #false: (), [], {}, 0, None
    a = [] #보통 다른 곳에서 데이터를 가져오고
    if a: # 이 함수를 통해 제대로 데이터를 긁어왔는지를 확인
        print(True)
    else:
        print(False)  
          
false_iterable()

# 6. any(x): all(x)의 반대, 하나라도 참이면 True
def in_any():
    print(any([1, 2, 3, 4, 5])) #True
    print(any([(), [], {}, 0, None])) #False
    
# 7. eval(exp): 문자열로 구성된 표현식을 입력받아, 
#               해당 문자열을 실행할 결과를 리턴하는 함수
print(eval('1+1')) # 2
print(eval('"1" + "2"')) #12
var_str = '[]'
var_eval = eval(var_str) #파일에서 데이터를 갖고 올 때 string으로 받게 될 수 있음. 
#그럴 경우, 전체 데이터를 list로 변환해주기 위해 eval로 바꿔줌
#list 함수를 쓰지 않는 이유는 데이터 하나 하나가 다 리스트로 전환되기 때문
print(type(var_str), type(var_eval)) #<class 'str'> / <class 'list'>

# 8. filter(함수, 반복 가능한 데이터): 만든 데이터 중에서 필요한 데이터를 뽑아올 때 사용
# 반복 가능한 데이터를 하나씩 뽑아와서 함수에 넣는다
# 리스트를 입력값으로 넘겨서 리스트로 결과값을 받아온다
# ex) list안에서 양수인 값만 가져오기

def positive_list(var_list):
    result = []
    for i in var_list:
      if i > 0:
          result.append(i)
    return result
var_list1 = positive_list([1, 2, 3, -2, 10, -5])
print(var_list1) 

def positive(x):
    return x > 0
print(list(filter(positive, [1, 2, 3, -2, 10, -5])))

#lambda
print(list(filter(lambda x : x > 0, [1, 2, 3, -2, 10, -5])))
#위의 3가지 코딩이 모두 같은 것

# 9. id(object): 객체의 고유 주소값을 리턴
def in_id():
    a = b = 3 # 주소값이 서로 같음
    print (id (a), id(b))
    b = 4
    print(id (a), id(b)) #b의 신규 주소가 생기면서, 주소값이 서로 달라짐


#함수변수 개념 확인
var_list = [1, 2, 3]
print(1, id(var_list))

def id_check():
    print(2, id(var_list)) #전역변수로 간주해서 위의 변수와 주소값이 같음
    var_list.append(4)
    print(3, id(var_list)) # 똑같은 저장소에 4가 추가되는 것 


# def id_check2():    
#     print(4, id(var_list)) # var_list는 해당 함수 내에서 사용되는 로컬변수로 간주 
#     var_list = [6 ,7 ,8]
#     print(5, id(var_list))

id_check() # 정상
# # id_check2() error 발생 

#오류를 안나게 하기 위해서는 
def id_check2():    
    global var_list
    print(4, id(var_list)) # 이전 값은 삭제되게 됨
    var_list = [6 ,7 ,8]
    print(5, id(var_list))

id_check2()

# 10. max(iterable)
def in_max():
    print(max([1, 20, 3])) #20
    print(max([(1, 2), (20, -3), (3,40)])) #20, -3 / 첫번째 인자가 큰 값을 추출
    print(max(['가', '나', '다'])) #다 가장 나중의 letter가 max
    print(max(['A', 'B', 'C'])) # C 가장 나중의 letter가 max
    print(max(['A', 'a'])) # a 소문자가 max
    print(max(['A', 'a', '가'])) #한글이 알파벳보다 max

def in_min():
    print(min([1, 20, 3])) #20
    print(min([(1, 2), (20, -3), (3,40)])) #20, -3 / 첫번째 인자가 큰 값을 추출
    print(min(['가', '나', '다'])) #다 가장 나중의 letter가 max
    print(min(['A', 'B', 'C'])) # C 가장 나중의 letter가 max
    print(min(['A', 'a'])) # a 소문자가 max
    print(min(['A', 'a', '가'])) #한글이 알파벳보다 max
