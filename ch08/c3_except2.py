try: # 자바의 try-catch
    print("정수를 입력하세요")
    x = int(input())
    y = 100/x
    print(f"나눗셈 결과 : {y}")
except ZeroDivisionError as err:
    print(f"0으로 못나눠 {err}")
except ValueError as err:
    print(f"정수가 아니야 {err}")