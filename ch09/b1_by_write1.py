file = open('bin.txt', 'wb')
file.write("안녕하세요".encode())
file.close()

file = open("bin.txt", 'rb')
txt = file.read()
# print(txt)
print(txt.decode())
file.close()