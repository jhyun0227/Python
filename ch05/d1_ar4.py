# 가변 매개변수 뒤에 정의 된 일반 변수를 호출할 때는 키워드 형식으로 해야함
def ar(*args, len):
    for i in range(len):
        print(args[i])
ar("대박", "사건", "야호", "금요일", len=4)