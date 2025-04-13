'''
1. 가위, 바위, 보 게임
    가위, 바위, 보 중에 하나를 input으로 받기
    컴퓨터는 랜덤으로 가위, 바위, 보 중에 하나 선택
    결과 출력
    == 출력 ==
    가위, 바위, 보 중에 하나를 선택하세요. : [가위]
    컴퓨터의 선택 : [보]
    당신이 이겼습니다. / 비겼습니다. / 컴퓨터가 이겼습니다. 
    
    2. 코딩순서
    1) input으로 가위, 바위, 보 하나 받기
    2) 가위, 바위, 보가 아니면 error 다시 선택해주세요.
    3) 컴퓨터가 랜덤 (radom.choice)으로 가위, 바위, 보를 선택
    4) 결과값을 if 문으로 출력하기
    
'''

import random 

choices = ["가위", "바위", "보"] # step1. 

while True:
    while True:
        user_choice =input("가위, 바위, 보, 종료 중에 하나를 선택하세요 : ") #step3. 
        if user_choice not in choices: #step4. 가위, 바위, 보가 아니면 다시 선택해주세요.
            if user_choice != "종료":
                print("다시 선택해주세요.")                
        # if user_choice != "가위" and user_choice !="바위" and user_choice !="보":
        #     print("다시 선택해주세요.")
            else:
                break
        else:
            break
          
    if user_choice == "종료":
        print("가위, 바위, 보 게임을 종료합니다.")
        break
      
    print(f"당신의 선택은 {user_choice}입니다.")

    computer_choice = random.choice(choices)
    print(f"컴퓨터의 선택은 {computer_choice}입니다.")

    #승부체크
    if user_choice == computer_choice:
        print("비겼습니다")

    elif (user_choice == "가위" and computer_choice == "보") or \
        (user_choice == "바위" and computer_choice == "가위") or \
        (user_choice == "보" and computer_choice == "바위"):
        print("당신이 이겼습니다.")

    else: 
        print("컴퓨터가 이겼습니다.")

print("end")