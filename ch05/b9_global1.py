def f():
    # x = 1 # 함수 내에서 정의한 변수는 지역변수
    print("함수 내 : ", x)
x = 7 # 밖에서 정의한 전역 변수는 함수 내에서도 사용이 가능
f()
print("함수 밖 : ", x) # 지역변수는 함수밖에서 사용 못함