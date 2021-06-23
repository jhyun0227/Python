from socket import *
svrsocket = socket(AF_INET, SOCK_STREAM) # 소켓 객체 생성
svrsocket.bind(('127.0.0.1', 8000)) # 소켓을 컴퓨터 포트에 연결
svrsocket.listen(1) # 한 명을 연결
conn, addr = svrsocket.accept() # 클라이언트가 연결할때 까지 대기
print(addr)
b = conn.recv(1024) # 클라이언트가 보낸 글 읽기
conn.send("Hello Client".encode()) # 클라이언트에 직열화 하여 보내기
print(b.decode()) # 보낸 메세지를 역직열화
conn.close()