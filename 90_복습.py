mail_info = [
  {
    'sender':'GS편의점',
    'date':'2025-04-10 12:00',
    'subject':'할인이벤트',
    'detail':'4월 할인이벤트'
  },
  {
    'sender':'쿠팡',
    'date':'2025-04-11 11:00',
    'subject':'배송안내',
    'detail':'배송이 출발했어요'
  }
]
# 출력물: 보내는사람: GS편의점, 날짜: 2025-04-10 12:00, 제목: 할인이벤트, 내용: 4월 할인이벤트

#if mail_info:
for mail in mail_info: # mail => {'sender':'GS편의점','date':'2025-04-10 12:00','subject':'할인이벤트','detail':'4월 할인이벤트'} 
    # print(mail['sender'])
    print(f"보내는사람: {mail['sender']}, 날짜: {mail['date']}, 제목: {mail['subject']}, 내용: {mail['detail']}")
    
## class 
class FourCal:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  
  def add(self):
    return self.num1 + self.num2
  
fourcal = FourCal(10,20)
var_add = fourcal.add()
print(var_add)

class Morecal(FourCal):
  def sub(self):
    return self.num1- self.num2
  
morecal = Morecal(100,10)
var_sub = morecal.sub()
print(var_sub)