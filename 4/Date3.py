import datetime

today = datetime.datetime.now()

# 요일에 따른 메시지 출력하기
if today.weekday() == 5 or today.weekday() == 6:
    print("오늘은 주말입니다.")
    print("충전하는 시간을 가지세요!")
elif today.weekday() == 4:
    print("오늘은 금요일.")
    print("내일부터 주말입니다.")
else : 
    print("오늘은 출근하는 날입니다.")

# 배열로 같은 로직 구현하기
if today.weekday() in [5, 6]:
    print("오늘은 주말입니다. 충전하는 시간을 가지세요!")
elif today.weekday() in [0, 4]:
    print("오늘은 평일입니다. 출근하세요!")