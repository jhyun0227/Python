input1 = input("첫번째 숫자를 입력하세요. : ")
input2 = input("첫번째 숫자를 입력하세요. : ")
# 입력된 값은 문자로 인식한다.
total = input1 +input2
# 정수로 변경한 후 연산해야 함
total2 = int(input1) + int(input2)
print("두 수의 합 : ", total)
print("두 수의 합 : ", total2)
