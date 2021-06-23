sum = 0
for i in range(1, 101): # 1부터 101의 앞(100)까지
    sum += i
print(f"1부터 {i}까지 합은 {sum}")

for i in range(4): # 0부터 4바로 앞(3)까지
    print(f"i = {i}", end=" ")
    for j in range(4):
        print(j, end=" ")
    print();