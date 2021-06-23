from random import randint
lotto = set()
while len(lotto) < 6:
    ran = randint(1, 45) # 1 ~ 45 사이의 정수 random하게 발생
    lotto.add(ran)
print("로또번호 : ", sorted(lotto))