def f(a):
    a[0] = 100
    print("함수 내 : ", a)
# list, tuple, dic, 객체(변수가 여러개 값을 가진 경우)인 경우에는 주소를 전달
a = [1, 2, 3]
f(a)
print("함수 밖 : ", a)