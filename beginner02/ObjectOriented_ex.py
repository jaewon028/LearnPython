# - * - coding: utf-8 - * -
# 오름차순/내림차순으로 정렬하기

'''
 Studnet Class
 - 프라이빗 필드를 가지고 있음
 - 읽기 전용 name, gender의 프로퍼티
 - 읽기, 쓰기 모두 가능한 height 프로퍼티
 - 특수함수 __repr__에 대한 정의를 가짐
'''

class Student:

    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property
    # name property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    # 객체 출력할때 많이 사용할 때, 객체의 표현을 지원해줌.
    def __repr__(self):
        return "{}(name: {}, gender: {}, height: {})".format(self.__class__.__name__, self.name, self.gender, self.height)

# s1 = Student("홍길동", "남", 176.5) # repr 함수를 취함 : 객체 출력시 주로 사용
# print(s1)

# studnets 리스트 객체 생성
students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2)
]

for student in students:
    print(student)

# name 기준 오름차순 정렬
print("name으로 오름차순 정렬 후 ===>") # sorted : 반복 가능한 객체 대상.
# 사용자 정의 객체 사용 시 해당 리스트 객체에 있는 각 항목에서 키를 사용한 정보 전달
for student in sorted(students, key=lambda x: x.name, reverse=False): #reverse는 False가 디폴트
    print(student)

print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
    print(student)

print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)