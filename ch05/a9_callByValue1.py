def f(a):
    a = 7
    print('함수 내 a = ', a)
a = 10
f(a) # 전달되는 것은 a의 주소가 아니라 10이라는 값이 전달
print("요청 a = ", a)