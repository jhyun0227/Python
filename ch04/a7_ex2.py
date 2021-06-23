#    01234567890123456789
s = "usr/local/bin/python"
# 경로 : "usr/local/bin, 파일명 : python
# 뒤에서 부터 찾아서 발견되는 첫번째 / 인덱스의 값
index = s.rfind("/")
print("경로 : ", s[:index])
print("파일명 : ", s[index+1:])