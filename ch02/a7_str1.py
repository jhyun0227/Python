# 문장속에 작은 따옴표가 있을 경우 밖을 큰 따옴표로
str1 = "Python's favorite food is perl"
print("str1 = ", str1)
# 밖을 작은 따옴표로 했을 경우 \를 추가 해야 한다.
str2 = 'Python\'s favorite food is perl'
print("str2 = ", str2)

# 문장속에 큰 따옴표가 있는 경우에는 밖을 작은 따옴표로
str3 = '"Python is very easy." he says.'
print('str 3 = ', str3)
# 밖을 큰 따옴표로 했을 경우에는 \를 추가 해야 한다.
str4 = "\"Python is very easy.\" he says."
print('str 4 = ', str4)
