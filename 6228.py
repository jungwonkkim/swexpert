#6228. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 6

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print('정사각형의 면적: {}'.format(self.length * self.length))


s1 = Square(3)

s1.area()