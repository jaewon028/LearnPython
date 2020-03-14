# 객체지향 프로그래밍

# 멤버들의 이름과 나이를 관리하기 위한 프로그램 : 딕셔너리 객체 필요
members = [
    {"name" : "홍길동", "age": 20},
    {"name" : "이순신", "age": 45},
    {"name" : "강감찬", "age": 35},
]

for member in members:
    print("{} \t {}".format(member["name"], member["age"]))

def create(name, age):
    return {"name": name, "age": age}


def to_str(person):
    return "{}\t{}".format(person["name"], person["age"])


members = [
    {"name" : "홍길동", "age": 20},
    {"name" : "이순신", "age": 45},
    {"name" : "강감찬", "age": 35},
]

for member in members:
    print(to_str(member))

'''
클래스 정의
 class 클래스명 : 
 ....
 
 
객체 생성
 변수 = 클래스명() # 생성자 메서드 : 클래스 이름과 동일한 메서드
 !!!!! 클래스의 코드 블록 안에 필드와 메서드를 정의해 사용할 수 있음
'''

class Person:
    pass

member = Person() # member객체 생성

if isinstance(member, Person):
    # 첫 번째 인자의 객체가 두 번째 인자의 클래스 인스턴스인지 검사
    print("member는 Person 클래스의 인스턴스입니다.")

'''
객체의 생성과 소멸, 그리고 self

객체를 생성하기 위해 호출하는 생성자 메서드 ==> __init__ 
객체가 소멸되기 전에 호출되는 소멸자 메서드 ==> __del__
'''

'''
클래스 생성자 메서드 정의
class 클래스명:
    def __init__(self, 매개변수목록):
        ...
        
class 클래스명:
    ...
    def __del__(self):
        ...

!!!! self를 제외한 매개변수는 사용하지 않음
!!!! self는 객체 공간을 가리키는 식별자
!!! 객체 공간의 필드와 메서드에 접근할 경우 self. 식별자 형식을 이용


!!!
들어가기 전에 : 변수명에 홑밑줄(_)과 겹밑줄(__)이 있습니다.

홑밑줄(single underscore) : 보통 내부적으로 사용하는 변수일 때 사용합니다.

곁밑줄(double underscore) : 클래스 외부에서 접근할 수 없도록 내부 변수로 만듭니다.
'''
print("*"*50)
class Person:
    # self가 가리키는 객체공간에 name, age 필드 생
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.name))

member = Person("홍길동", 20)

print("{}\t{}".format(member.name, member.age))
print(dir(member))





# 인스턴스 메서드
# self가 가리키는 객체의 필드 정보에 접근 특정 목적의 기능을 수행하도록 정의된 메서드

print("*"*50)
class Person:
    # self가 가리키는 객체공간에 name, age 필드 생
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.name))

    def to_str(self):
        return "{}\t{}".format(self.name, self.age)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹

]

members[0].age = -20

for member in members:
    print(member.to_str())


print("#"* 60)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return  "{}\t{}".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise TypeError("나이만 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹

]

# members[0].set_age(-20)

for member in members:
    print(member.to_str())


print("=" * 50)

# 데코레이터 기능
'''
class Person:
    ...
        
        @property의 이름.setter
        def name(self):
        # 변수 이름과 같은 메서드를 만들어 사용 가능
'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self): # 변수처럼 사용 가능. __name 필드값을 반환하는 getter 메서드의 역할
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹

]

members[0].age = 22

for member in members:
    print(member.to_str())

print("=" * 50)

# 클래스 변수의 정의 및 접근
'''
 클래스 변수 정의
 class 클래스명:
    클래스변수 = 값
    ...

 클래스 변수 접근
 클래스명.클래스변수
'''
class Person:
    count = 0

    def __init__(self, name, age): # 객체가 생성될 때마다 호출되는 __init__ 메서드
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self):  # 변수처럼 사용 가능. __name 필드값을 반환하는 getter 메서드의 역할
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age


members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹
]

print("현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(Person.count))

print("*" * 80)

# 클래스 메서드 : 클래스가 소유한 메서드
'''
class 클래스명:
    ...
    @classmethod
    def 클래스메서드(cls, 매개변수목록):
        ...
        # cls: 클래스 자신에 대한 참조 전달

클래스 메서드의 사용 
클래스명.클래스메서드명

'''

class Person:
    count = 0

    def __init__(self, name, age): # 객체가 생성될 때마다 호출되는 __init__ 메서드
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self):  # 변수처럼 사용 가능. __name 필드값을 반환하는 getter 메서드의 역할
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count) #Person.count와 동일

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹
]

print(Person.get_info())


print("&" * 80)

# 연산자 오버로딩


class Person:
    count = 0

    def __init__(self, name, age): # 객체가 생성될 때마다 호출되는 __init__ 메서드
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{} 객체가 생성되었습니다.".format(self.__name))

    def __del__(self):
        print("{} 객체가 제거되었습니다.".format(self.__name))

    def to_str(self):
        return "{}\t{}".format(self.__name, self.__age)

    @property
    def name(self):  # 변수처럼 사용 가능. __name 필드값을 반환하는 getter 메서드의 역할
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {} 개입니다.".format(cls.count) #Person.count와 동일

    def __gt__(self,other):
        return self.__age > other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age

    # __str()__ 메서드
    # 메서드 구현 => str() 함수에 객체를 전달해 문자열로 변환
    def __str__(self):
        return "{}\t{}".format(self.__name, self.__age)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
    # Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성.옹
]

cnt = len(members)
i=0
while True:
    print("members[{}] > members[{}] => {}".format(i, i+1, members[i] > members[i+1]))
    i+=1
    if i == cnt - 1:
        print("members[{}] > members[{}] => {}".format(i, 0, members[i] > members[0]))
        break

print("============================ 클래스 상속 ==============================")
# 동작의 재사용, 확장, 수정 !!!! 단일상속만 지원!!
'''
클래스 상속
class 클래스명(부모클래스명):
'''
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")

    @property
    def family_name(self):
        return self.__family_name


class Child(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name) # 부모 클래스의 패밀리네임 필드를 매개변수 라스트네임으로 초기화
        # super().__init__(last_name) 위 문장과 동일한 결과
        self.__first_name = first_name # 매개변수 first_name에 의해 초기화됨.
        print("Child 클래스의 __init__() ...")




