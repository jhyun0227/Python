file = open("chicken.txt", 'r', encoding='utf-8')
# print(type(file)) file의 데이터 타입

for i in file:
    print(i, end="")
file.close()