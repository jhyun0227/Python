def f1(count):
    if count > 0:
        print(count, '현재')
        f1(count - 1) # 조건을 변경하지 않으면 무한 루프
    print('결과', count)

f1(6)