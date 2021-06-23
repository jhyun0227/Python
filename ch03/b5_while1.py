sum = 0
cnt = 1
# while은 조건이 맞으면 true 아니면 false
while cnt <= 100:
    sum += cnt
    cnt += 1
else: # python에서는 else가 추가, 생략 가능
    print(f"현재 cmt숫자는 {cnt}입니다.")
print(f"합계 : {sum}")