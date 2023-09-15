import random

uName = input("당신의 이름을 입력해주세요: ").upper().strip()
pw = input("암호를 입력해주세요: ")
print ("반갑습니다.", uName,  "님. 가위바위보를 시작합니다.")
print()

cChoice = random.choice("RSP")
uChoice = input("R(바위), S(가위), P(보) 중 하나를 입력해주세요.").upper().strip()

if(pw == '묵찌빠'):
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