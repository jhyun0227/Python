import threading, time
def ThreadEx(id):
    for i in range(10):
        print(f"id : {id}, {i}")
        time.sleep(1) # 1초 대기
for i in range (2):
    id = (f"{i}번 쓰레드")
    # target은 실행할 함수 args는 전달할 데이터
    th = threading.Thread(target=ThreadEx, args=(id,))
    th.start()