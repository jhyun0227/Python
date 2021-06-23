x = [2, 3, 5, 7, 11]
y = x # 주소를 복사해 준다. y를 alias(별칭)
k = list(x) # list함수를 사용하여 데이터 값을 복사
y[2] = 77
print(x)
print(y)
print(k)