class A:
    attr = "정적 클래스"

ob1 = A()
print(ob1.attr)

# 클래스명     생성     속성
ob2 = type('B', (), {'attr' : '동적 클래스'})
print(ob2.attr)