#6217. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 3 


class Student:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'이름: {self.name}')

class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def info(self):
        print(f'이름: {self.name}, 전공: {self.major}')


s1 = Student('홍길동')
s2 = GraduateStudent('이순신','컴퓨터')

s1.info()
s2.info()
