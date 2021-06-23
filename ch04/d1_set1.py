# list = [] or list = list()
# set = set()
s1 = set()
# s1 = {} 안됨, dictionary도 {} 사용
print(s1)
s2 = {1, 2, 3}
print(s2)
s3 = set({1, 2, 3, 2}) # 튜플
print(s3) # set의 값은 중복되지 않는다.
s4 = set("hello world")
print(s4) # 각각의 문자를 값으로 생각하고 처리하는데 중복단어는 한번만
s5 = set([1, 2, 3]) # list
print(s5)