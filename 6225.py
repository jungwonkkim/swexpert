#6225. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 5

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f'사각형의 면적: {self.length * self.width}')


r1 = Rectangle(4,5)
r1.area()