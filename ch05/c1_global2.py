def f():
    global a # 함수 내의 변수와 함수 밖의 변수를 통일하여 사용
    a += 1
    print("함수 내 : ", a)

a = 7
f()
print("함수 밖 : ", a)

def outer():
    a = 1
    def inner():
        nonlocal a
        print("함수의 외부 함수에 있는 a:{0}".format(a))
        a = 10
    inner()
    print("내부함수에서 변경한 경우의 a:{0}".format(a))
a = 0
outer()
print("a:{0}".format(a))