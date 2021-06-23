class Call1:
    def __call__(self, *args, **kwargs):
        print("누가 날 불렀네")

ob = Call1()
ob() # 객체를 메서드처럼 호출하면 call 메서드 실행