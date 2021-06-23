a = [1, 2, 3]

a.insert(0, 4) # 인덱스 자리에 숫자를 추가
print(a)

a.insert(2, 5) # 인덱스 자리에 숫자를 추가
print(a)

a.remove(2) # 인덱스 값이 아닌 배열의 첫번째 2의 값을 제거
print(a)

print(a.pop()) # 마지막 데이터를 끄집어 출력하고 삭제
print(a)

print(a.pop(0)) # 인덱스 0번의 데이터를 끄집어 출력하고 삭제
print(a)