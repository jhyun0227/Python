num = [1, 2, 3, 4, 5]
result = []
result2= []

# [2, 4, 6, 8, 10]
for i in num:
    result.append(i * 2)
print(result)

# 호루만
for i in num:
    if i % 2 == 1:
        result2.append(i * 2)
print(result2)