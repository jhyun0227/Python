#    012345
a = "Pithon"
# i가 y로 변경
# 문자열은 일부만 변경이 불가
# a[1] = 'y'
print(a[:1] + 'y' + a[2:])

#      012345678901234567
str = "Hardware and Shell"
print(str[:8] + ' Ker1nel ' + str[13:])
print(str[:8] + str[12:])