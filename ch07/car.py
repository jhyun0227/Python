class Car:
    def __init__(self): # 생성자 역할
        self.color = 0xff0000  # 속성, 멤버변수, 필드
        self.wheel_size = 16
        self.displacement = 2000
    def forward(self):  # method
        pass
    def backword(self):
        pass

my_car = Car()
print(my_car.wheel_size)