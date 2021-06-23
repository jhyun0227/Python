# 1~1000 3의 배수의 합
sum = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        sum += i
    i += 1
print("1부터 1000까지 3의 배수의 합 : ", sum)