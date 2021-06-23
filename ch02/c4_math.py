import math # 자바의 math 클래스와 유사
print(type(math.pi)) # 데이터타입을 확인
print("반지름이 {}인 원의 면적은 {}입니다.".format(10, math.pi*10*10))
# %d 정수, 0.2f 소숫점 두자리 실수
# 자바의 System.out.printf와 유사
print("반지름이 %d인 원의 면적은 %0.2f입니다." %(10, math.pi*10*10))
print('반지름이 '+str(10)+'인 원의 면적은 '+str(math.pi*10*10)+'입니다.')
print('반지름이 ', str(10), '인 원의 면적은', str(math.pi*10*10), '입니다.')