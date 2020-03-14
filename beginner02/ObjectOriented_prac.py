# 6203 OOP 01
'''
다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

입력
89, 90, 100

출력
국어, 영어, 수학의 총점: 279

'''


class Subject():
    count = 0
    sums = 0

    def __init__(self, kor, eng, mat):
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        Subject.count += 1
        print("{}번 객체가 생성되었습니다.".format(self.count))

    def __del__(self):
        print("{}번 객체가 제거되었습니다.".format(self.count))

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, kor):
        self.__kor = kor

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        self.__eng = eng

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, mat):
        self.__mat = mat

    @classmethod
    def get_info(cls):
        return "현재 클래스 갯수 : {} 개 입니다.".format(cls.count)

    def total(self):
        return self.mat + self.eng + self.kor

    # def to_str(self):
    #     return "국어, 영어, 수학의 총점 : {} ".format(self.__class__.__name__, self.total())

    def __repr__(self):
        return "국어, 영어, 수학의 총점 : {} {}".format(self.__class__.__name__, self.total())


score = input("OOP 01 Input : ").split(",")
student = Subject(int(score[0]), int(score[1]), int(score[2]))
print(student.total())
print(student)


# 6208 OOP 02
class Korean:
    def printNationality(self):
        print("대한민국")


koreans = Korean()
koreans.printNationality()

# 6217 OOP 03
'''
name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진

GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를

다음과 같이 문자열로 출력하는 코드를 작성하십시오.

출력
이름: 홍길동

이름: 이순신, 전공: 컴퓨터
'''
class Student:
    """Parnet/Super class"""
    _name1 = "홍길동"
    _name2 = "이순신"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def show(self):
        print("이름: "+self._name1)

class GraduateStudent(Student):
    """Child/Sub class"""
    __major = "컴퓨터"

    def __init__(self):
        self.__name = super()._name2

    def show(self):
        print("이름: {}, 전공: {}".format(self.__name, self.__major))


Student().show()
GraduateStudent().show()

# 오버라이드 예제 ( 상속 )
class Animal():
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

    def greet(self):
        print('인사한다')

class Cow(Animal):
    '''소'''

class Human(Animal): # 상속 : 클래스 괄호 안에 다른 (부모)클래스를 넣는 것
    def wave(self):
        print('손을 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wave()

class Dog(Animal): # Animal의 내용을 상속받는다
    def wag(self):
        print('꼬리를 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()

#super()
'''
자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
super().부모클래스내용
'''

class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )