# 곱셈/나눗셈 먼저, 덧셈, 뺄셈 나중에
print(2+3*2)
# 괄호가 있으면 우선 처리
print((2+3)*2)

# python에서는 정수는 메모리가 허용하는 한 제한이 없다.
a1 = 321687213218432168431218432154
print(a1)

# type은 데이터타입을 확인
print(type(a1))

# 정수형끼리 4칙 연산을 하면 정수지만 나눗셈은 결과가 실수(float)
print(8/2)
print(type(8/2))

a2 = 10/0
print('a2 = ', a2)