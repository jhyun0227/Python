import copy

a = [1, 2, 3]
b = a # list의 값이 아닌 list의 주소를 전달
c = list(a) # list 값을 전달
d = copy.copy(a) # 값을 복사해서 전달
a[0] = 11
print(a)
print(b)
print(c)
print(d)