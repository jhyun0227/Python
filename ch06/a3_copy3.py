import copy

a = [1, 2, 3]
x = [a, 100]
# 깊은 복사, 주소값에 해당하는 데이터 까지 값을 복사
y = copy.deepcopy(x) # 값을 복사
x[1] = 200

print(a)
print(x)
print(y)

x[0][0] = 77
print(x)
print(y)