import re

p = re.compile('a', 'b') #\n을 제외한 모든 문자
m = p.match('a\nb') # match 조건이 맞는지 확인
print(m) # 조건에 맞는것이 없다.
m = p.match('akb')
print(m)
m= p.match('a.b')
print(m)