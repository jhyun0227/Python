g1 = (n*n for n in range(21))
print(g1)
# List와 비슷하지만 소괄호로 처리
g2 = (n*n for n in range(21))
# li = list(g2)
# print(li)
# print(type(g2))
for i in range(10):
    val = next(g2)
    print(val)
print("=========================")
# 제너레이터로 생성하면 yield처럼 사용된 것을 제외하고 다음 것이 반영
for i in g2:
    print(i)