# 문자는 default, 10칸 확보하고 왼쪽부터 채워라
print("안녕 {0:10}님.".format('길동'))
# 왼쪽부터
print("안녕 {0:<10}님.".format('길동'))
# 오른쪽부터
print("안녕 {0:>10}님.".format('길동'))
# 중앙부터
print("안녕 {0:^10}님.".format('길동'))
# 왼쪽부터 빈 공간은 #으로
print("안녕 {0:#<10}님".format('길동'))
# 오른쪽부터 빈 공간은 #으로
print("안녕 {0:#>10}님".format('길동'))
# 중앙부터 빈 공간은 #으로
print("안녕 {0:#^10}님".format('길동'))
# 10칸 확보 소숫점 2자리
print("{0:10.2f}".format(3.1415923))