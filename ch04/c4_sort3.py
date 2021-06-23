# 대소문자 구별하고 소문자보다 대문자가 크다
data = ['Morning', 'Afternoon', 'evening', 'Night']
data.sort()
print(data)
data.sort(reverse=True)
print(data)

# 대소문자 구별 없이 정렬
data.sort(key=str.lower, reverse=True)
print(data)