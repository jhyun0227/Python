print("피보나찌 몇개")
n = int(input())
a = [1, 1]
for b in range(2, n):
    a.append(a[b-2]+a[b-1])
print(a)
print(f"{n}번째 값 {a[n-1]}")