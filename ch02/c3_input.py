print("숫자를 입력하세요")
# input으로 받는 데이터는 문자열로 취급한다.
a = int(input())
print("숫자를 입력하세요")
b = input()
print(a * int(b)) # 숫자로 연산하기 위해서는 int 또는 float로 형변환을 해야한다.
print("{} * {} = {}".format(a, b, a*int(b))) # 자바의 String.format과 유사