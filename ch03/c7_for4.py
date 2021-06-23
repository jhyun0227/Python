# 주사위를 두번 던져 합이 4의 배수인 경우 출력
for i in range(1, 7):
    for j in range(1, 7):
        k = i + j
        if k % 4 == 0:
            print(f"{i} + {j} = {i+j}")