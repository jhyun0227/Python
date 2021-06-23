a, *b = [1, 2, 3, 4, 5] # 1은 a에, 나머지는 모두 b에
print(a)
print(b)

*a, b = [1, 2, 3, 4, 5] # 5는 b에 나머지는 모두 a에
print(a)
print(b)

a, *b, c = [1, 2, 3, 4, 5] # 1은 a에 5는 c에 나머지는 b에
print(a)
print(b)
print(c)

# a, *b, *c = [1, 2, 3, 4, 5] b와 c에 들어갈 갯수가 불명확하여 에러