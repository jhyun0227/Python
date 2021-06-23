def fat1(num):
    result = 1
    # 1*2*3
    # 1*2*3*4*5
    for i in range(1, num+1): # 1부터 num까지 순차적으로 i에 대입
        result *= i
    return result

print(fat1(3))
print(fat1(5))