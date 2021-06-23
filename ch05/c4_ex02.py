# *가 붙은 변수에는 여러개의 값이 전달
def average_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

print("평균 : ", average_numbers(10, 20, 30))
print("평균 : ", average_numbers(10, 12, 16))
print("평균 : ", average_numbers(1, 2, 3, 4, 5))