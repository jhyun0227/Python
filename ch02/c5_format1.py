li = [1, 6 ,3]
# {1:3d} 1은 format 뒤에 있는 인덱스 번호, 3은 3칸 확보, d는 정수
print("최대값:{1:3d}\t최소값:{0:5d}".format(max(li), min(li)))

#      0123456789012345
str = "c:/data/data.txt"
# test있는지 확인
print(str.find('test')) # test가 있으면 test가 시작하는 index 번호보여주고 없으면 -1
print(str.find('.'))
print(str.rfind('.'))
print(str.find('/')) # 앞에서부터 /를 찾아서 첫번째 발견된 /의 index
print(str.rfind('/')) # 뒤에서부터 /를 찾아서 첫번째 발견된 /의 index

n = str.find('.')
print('확장자 : ', str[n+1:]) # str에서 (12+1)부터 끝까지 출력
#폴더명
m = str.rfind('/')
print("패키지명 : ", str[:m])

# str을 매개변수를 기준으로 배열을 만들기
list = str.split(".")
print(list)

# 총글자 수
print("총 글자 수 : ", len(str))

# 배열 갯수
print('배열 갯수 : ', len(list))

# 확장자
print('확장자 : ', list[len(list) - 1])

# 데이터를 Python을 변경
print(str.replace('data', 'python'))