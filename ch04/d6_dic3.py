d1 = {} # {} dictionary로 인식 / set은 set()으로 써야함
print(type(d1))

# key는 중복되어서는 안됨
d1[5] = 25 # dict명[key] = 값
d1[2] = 4
d1[3] = 9
d1[3] = 12 # key가 중복일 경우 앞의 key의 값을 덮어쓴다 / 마지막 입력된 값으로 출력 된다.
print(d1)
print(d1[5])
print(d1.get(3)) # get() 함수에 key를 넣어 값을 가져올 수 있다.
print(d1.get(4)) # key에 해당하는 값이 없으면 None
print(d1.get(4, "대박")) # 두번째 파라미터는 해당하는 값이 없을 때 default로 보여주는 값
print(5 in d1) # in은 key에 있는지 여부
print(4 in d1)
print(5 not in d1) # not in은 key에 없는지 여부
print(4 not in d1)
print(d1.keys()) # key만 출력
print(d1.values()) # 값만 출력

d1.clear() # data 전부 삭제
print(d1)