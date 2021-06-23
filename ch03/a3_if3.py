# print("요일의 첫글자를 입력하세요.")
# elif는 자바에서 else if 와 같다.
week = input("요일의 첫글자를 입력하세요 : ")
if week == "월":
    result = "Monday"
elif week == "화":
    result = "Tuesday"
elif week == "수":
    result = "Wednesday"
elif week == "목":
    result = "Thursday"
elif week == "금":
    result = "Friday"
elif week == "토":
    result = "Saturday"
elif week == "일":
    result = "Sunday"
else:
    result = "아으어"
print(result)