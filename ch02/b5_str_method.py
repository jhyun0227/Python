#    01234
a = "Hello"
# startswith 함수는 문자열이 매개변수 값으로 시작하는지 판단
print(a.startswith("H"))
# endswith 함수는 문자열이 매개변수 값으로 끝나는지 판단
print(a.endswith("o"))
print(a.endswith('h'))
# find 함수는 매개변수 값이 문자열의 몇 번째 인덱스인지
print(a.find("l"))
# rfind 함수는 매개변수 값이 문자열의 뒤에서부터 찾아서 몇 번째 인덱스인지
print(a.rfind("l"))
# count 함수는 매개변수의 값이 문자열에서 몇 개를 가지고 있는지
print(a.count("l"))

b = "ABCdef"
# isalpha 함수는 알파벳인지 아닌지 판단
print(b.isalpha())
# isalnum 함수는 알파펫 또는 숫자인지 판단
print(b.isalnum())
# isnumeric 함수는 숫자인지 아닌지 판단
print(b.isnumeric())
# upper 함수는 문자열을 대문자로 변경
print(b.upper())
# lower 함수는 문자열을 소문자로 변경
print(b.lower())

c = "Hello, World"
# replace 함수는 문자열에서 첫 번째 매개변수와 동일 한 문자열을 두 번째 매개변수 값으로 변경
print(c.replace("Hello", "안녕"))
# split 함수는 매개변수의 값을 기준으로 문자열을 분리해서 list로 변경
print(c.split(', '))