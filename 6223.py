#6223. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 4 


class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r
    
    def area(self):
        print(f'원의 면적: {self.pi*self.r*self.r}')


c1 = Circle(2)
c1.area()