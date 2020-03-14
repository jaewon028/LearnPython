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

