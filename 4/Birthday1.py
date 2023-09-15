# 날짜 계산 프로그램 만들기

import datetime

# 사용자 입력 얻기
year = input("태어난 해는 언제인가요? ")
year = int(year)
month = input("태어난 달은 언제인가요? ")
month = int(month)
day = input("태어난 날은 언제인가요? ")
day = int(day)

# 날짜 만들기
bday = datetime.datetime(year, month, day)

# 결과 출력하기
# if bday.weekday() == 6:
#     print("일요일에 태어나셨군요!")
# elif bday.weekday() == 0:
#     print("월요일에 태어나셨군요!")
# elif bday.weekday() == 1:
#     print("화요일에 태어나셨군요!")
# elif bday.weekday() == 2:
#     print("수요일에 태어나셨군요!")
# elif bday.weekday() == 3:
#     print("목요일에 태어나셨군요!")
# elif bday.weekday() == 4:
#     print("금요일에 태어나셨군요!")
# elif bday.weekday() == 5:
#     print("토요일에 태어나셨군요!")

# 다른 방법으로 결과 출력하기
if bday.weekday() == 6:
    dow = "일"
elif bday.weekday() == 0:
    dow = "월"
elif bday.weekday() == 1:
    dow = "화"
elif bday.weekday() == 2:
    dow = "수"
elif bday.weekday() == 3:
    dow = "목"
elif bday.weekday() == 4:
    dow = "금"
elif bday.weekday() == 5:
    dow = "토"
print("당신이 태어난 날은", dow, "요일입니다.")