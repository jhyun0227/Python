print("아이디를 입력하세요.")
id = input()
print("암호를 입력하세요")
password = input()

if id=="root":
    if password=="system":
        print("로그인 성공")
    else:
        print("틀린 암호입니다.")
else:
    print("없는 아이디 입니다.")