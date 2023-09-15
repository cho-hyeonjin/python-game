import random

# 컴퓨터가 하나 고르기
cChoice = random.choice("RSP")

# 사용자를 입력한 가위바위보
uName = input("당신의 이름은? ").strip()
print()
print ("어서오세요,", uName, "님. '가위바위보'를 시작하겠습니다.")
print()

# 사용자 선택 얻기
# print("Rock, Scissors, Paper?")
uChoice = input("R(바위), S(가위), P(보) 중 하나를 고르세요: ").upper().strip() # 사용자가 소문자를 입력하면 대문자로 바꾸고, 공백을 입력한 경우 삭제처리까지!
print()

# 테스트하기
# print("당신: ", uChoice)
# print("컴퓨터: ", cChoice)


if(uChoice==cChoice):
    print("비겼습니다.")
elif(uChoice == "R" and cChoice == "P"):
    print("졌습니다. / 당신: 바위, 컴퓨터: 보자기")
elif(uChoice == "P" and cChoice == "R"):
    print("이겼습니다. / 당신: 보자기, 컴퓨터: 가위")
elif(uChoice == "S" and cChoice == "R"):
    print("졌습니다. / 당신: 가위, 컴퓨터: 바위")
elif(uChoice == "R" and cChoice == "S"):
    print("이겼습니다. / 당신: 바위, 컴퓨터: 가위")
elif(uChoice == "P" and cChoice == "S"):
    print("졌습니다. / 당신: 보자기, 컴퓨터: 가위")
elif(uChoice == "S" and cChoice == "P"):
    print("이겼습니다. / 당신: 가위, 컴퓨터: 보자기")
else:
    print(uName, ", 게임 설명을 또 듣는 일은 지겨울 거에요. 그렇죠? R, S, P 중 하나만 낼 수 있어요.")