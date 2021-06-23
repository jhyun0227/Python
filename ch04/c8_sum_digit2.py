# 자리수 합계 367 => 3+6+7, 564 => 5+6+4
print("점수를 여러자리 입력해 보세요.")
num = int(input())
sum = 0
while num != 0:
    sum += num%10 # 0+7 => 7+6 => 13+3
    num = num // 10 # 36 => 3 => 0
print(sum)