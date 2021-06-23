# 국적에 매개변수로 전달되지 않으면 default가 한국
def myself(name, age, nationality = "한국"):
    print("이름 : ", name)
    print("나이 : ", age)
    print("국적 : ", nationality)
    print("============================")
myself("길동", 23, "미국")
myself("영희", 47)