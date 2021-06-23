a1 = [1, 2, 3]
a2 = [4, 5 ,6]
a3 = '123'
print(a1 + a2) # list + list는 list형식
print(a1 * 3) # 반복
print(len(a1)) # 인덱스 갯수
print(str(a1[1])+'hi') # 숫자와 문자의 더하기는 에러

a1[1] = 7
print(a1)
# a3[1] = 7 문자열은 변경 불가

del a1[2:] # a1의 인덱스 2 이후 데이터를 삭제
print(a1)

a2.append(8) # append 함수는 배열의 맨뒤에 매개변수 값을 추가
print(a2)

a2.append([2,4]) # append 함수의 매개변수가 배열 인 경우 배열 자체를 추가  
print(a2)
