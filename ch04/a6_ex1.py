print("문자를 입력하세요.")
st = input()
print(st)
print(st[::-1])

l = len(st) - 1

while l >= 0:
    print(st[l], end="") # 인덱스는 0부터 시작
    l = l - 1
print()

# 마지막, 인덱스 -1 바로 앞 즉 인덱스 0까지, 인덱스 1씩 감소
for i in range(len(st) - 1, -1, -1):
    print(st[l], end="")
    l = l - 1
print()
