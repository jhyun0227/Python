a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print(b.difference(a)) # 차집합
print(a.symmetric_difference(b)) # 합집합-교집합
print(5 in a) # 포함 여부
print(7 in a)
print(5 not in a) # 불포함 여부
print(7 not in a)
