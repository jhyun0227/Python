file = open('chicken.txt','r', encoding='utf-8')
sum = 0
for i in file:
     # strip \n \t 공란 제거
    data = i.strip().split(": ")
    print("날자 :",data[0],"매출액 :", data[1]) # 날자, 금액
    sum += int(data[1])
print(f"매출액 합계 : {sum}")
file.close()