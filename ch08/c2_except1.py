try: # 자바의 try-catch
    print("정수를 입력하세요")
    x = int(input())
    y = 100/x
    print(f"나눗셈 결과 : {y}")
except ZeroDivisionError:
    print("0으로 못나눠")
except ValueError:
    print("정수가 아니야")