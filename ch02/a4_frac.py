# fractions의 패키지에서 Fraction이라는 클래스를 가지고 와서 사용하겠다.
# 자바에서는 import fractions.Fraction
# Fraction은 분수를 사용
from fractions import Fraction
#           분자 분모         분수 2/7
a1 = Fraction(5, 7) + Fraction('2/7')
print("a1 = ", a1)