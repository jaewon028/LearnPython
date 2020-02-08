# 1. abs()
# 인자로 숫자를 전달하면 그 숫자의 절대값을 반환하는 함수
val = 10
print("abs{} => {}".format(val, abs(val)))
val = -3.14
print("abs{} => {}".format(val, abs(val)))

# 2. divmod()
# 첫 번째 인자를 두 번째 인자로 나눴을 때의 몫과 나머지를 튜플 객체로 변환하는 함수
val1, val2 = 9, 5
result_tuple = divmod(val1, val2)
print("divmod{},{} => 몫: {}, 나머지: {}".format(val1, val2, *result_tuple))

# 3. pow()
# 첫 번째로 전달된 인자 값에 대해 두 번째로 전달된 인자 값으로 제곱한 결과를 반환하는 함수
data_list = [1,2,3,4,5]
print("pow({},2) => {}".format(data_list[2],pow(data_list[2],2)))

print("list(map(lamda x: pow(x, 2), {})) => {}".format(data_list, list(map(lambda x: pow(x,2),data_list))))

# 4. all()
# 반복 가능한 자료형인 List, Tuple, set, dictionary, 문자열 등을 인자로 전달하여
# 항목 모두가 True로 평가되면 True를 반환, false로 평가되는 항목이 하나라도 있다면 false를 반환하는 함수
val = [True, True, True]
print("all({}) => {}".format(val, all(val)))

val = [10, 20, 30]
print("all({}) => {}".format(val, all(val)))

val = [10, 20, 0]
print("all({}) => {}".format(val, all(val)))

val = [10, 20, ""]
print("all({}) => {}".format(val, all(val)))

val = [10, 20, False]
print("all({}) => {}".format(val, all(val)))

val = [10, 20, None]
print("all({}) => {}".format(val, all(val)))

# 5. any()
# 반복 가능한 자료형인 List, Tuple, set, dictionary, 문자열 등을 인자로 전달하여
# 항목 모두가 False로 평가되면 False를 반환하고, True로 평가되는 항목이 하나라도 있으면 True를 반환하는 함수
val = [True, True, True]
print("any({}) => {}".format(val, any(val)))

val = [10, 20, 30]
print("any({}) => {}".format(val, any(val)))

val = [10, 20, 0]
print("any({}) => {}".format(val, any(val)))

val = [10, 20, ""]
print("any({}) => {}".format(val, any(val)))

val = [10, 20, False]
print("any({}) => {}".format(val, any(val)))

val = [10, 20, None]
print("any({}) => {}".format(val, any(val)))

val = [False, False, False]
print("any({}) => {}".format(val, any(val)))

# 6. enumerate()
# List, Tuple, 문자열과 같은 시퀀스형을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환하는 함수
data_list = [10, 20, 30, 40, 50]

for idx, val in enumerate(data_list):
    print("data_list[{}]: {}".format(idx, val))

print("-"*25)

for obj in enumerate(data_list):
    print("{}: {}, {}".format(type(obj),obj[0],obj[1]))

print("-"*25)

for obj in enumerate(data_list):
    print("{}: {}, {}".format(type(obj), *obj))

# 7. filter()
# 조건에 해당하는 항목을 걸러내는 함수
def iseven(num):
    return num%2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

ret_val = filter(iseven, numbers) # Iseven 함수가 True를 반환한 짝수 값을 항목으로 하는 리스트 생성 후 반환
# ret_val = filter(lambda n: n%2==0, numbers)
print("{}".format(type(ret_val)))
print("{}".format(list(ret_val)))

# 8. list, tuple, set, dict
data_str = "Hello"

data_list = list(data_str)
print("list('{}') => {} {} ".format(data_str,type(data_list),data_list))

data_tuple = tuple(data_list)
print("list('{}') => {} {} ".format(data_list,type(data_tuple),data_tuple))

data_set = set(data_tuple)
print("list('{}') => {} {} ".format(data_tuple,type(data_set),data_set))

data_dict = dict(enumerate(data_set))
print("list('{}') => {} {} ".format(data_set,type(data_dict),data_dict))


print("=" *25)
# 9. map()
# 두 번째 인자로 반복 가능한 자료형을 전달 받아 자료형의 각 항목에 대해 첫 번째 인자로
# 전달 받은 함수를 적용한 겨과를 맵 객체로 변환하는 함수
data_list = list("abcdef")
result = list(map(lambda x: x.upper(), data_list))
print("list(map(lambda x: x.upper(), {})) => {} {}".format(data_list, type(result),result))

# 10. max(), min()
data_list = [10,25,30,45,50]
print("{0} => min: {1}, max: {2}".format(data_list, min(data_list),max(data_list)))

# 11. range()
# 첫 번쨰 인자로 전달된 시작 값
# 두 번째 인자로 전달된 종료 값
# 세 번째 인자로 전달된 증감치
# 주의! 종료 값으로 사용된 두번쨰 인자의 값은 포함되지 않음
data_list1 = list(range(0, 10, 1))
data_list2 = list(range(0, 10)) # 이 때, 생략된 세 번째 매개변수의 기본 값은 1로 설정
data_list3 = list(range(10)) # 생략된 첫 번째 매개변수의 기본 값은 0이고, 세 번째 매개변수의 기본값은 1로 설정

print("list(range(0, 10, 1)) => {}".format(data_list1))
print("list(range(0, 10)) => {}".format(data_list2))
print("list(range(10)) => {}".format(data_list3))

# 12. sorted()
# 반복 가능한 자료형을 인자로 전달받아 항목들로부터 정렬된 리스트를 생성해 반환하는 함수
data_list = [3, 8, 12, 2, 5, 11]
asc_result = sorted(data_list)
print("{} {}".format(type(data_list), data_list))
print("{} {}".format(type(asc_result), asc_result))
print("-" * 35)
desc_result = list(reversed(asc_result))
print("{} {}".format(type(data_list), data_list))
print("{} {}".format(type(asc_result), asc_result))
print("{} {}".format(type(desc_result), desc_result))

# 13. zip()
# 둘 이상의 반복 가능한 자료형을 인자로 전달받아,
# 동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip 객체를 생성하는 함수
# 주의! 인자로 전달된 객체는 동일 자료형이면서, 항목의 개수가 같아야 함
data_list1 = [1,2,3]
data_list2 = [4,5,6]
data_list3 = ["a","b","c"]

print("list(zip({}, {})) => {}".format(data_list1,data_list2, list(zip(data_list1, data_list2))))
print("list(zip({}, {})) => {}".format(data_list1,data_list2, list(zip(data_list1, data_list2, data_list3))))
print("dict(zip({}, {})) => {}".format(data_list3, data_list1, dict(zip(data_list3, data_list1))))

print("*****************변환 함수*****************")
# 14. chr(), ord(), hex()
# chr() : 정수 형태의 유니코드 값을 인자로 전달받아 해당 코드의 문자를 반환
# ord() : 문자를 인자로 전달 받아 유니코드값(10진 정수)을 반환
# hex() : 10진 정수 값을 인자로 전달 받아 16진수로 변환된 값을 반환하는 함수

# 15. int(), float(), str()
x = "10"
y = "3C"
z = 4.5

print("2진수 표현인 문자열 '{}' 는 10진수 {}로 변환됩니다.".format(x, int(x,2)))
print("16진수 표현인 문자열 '{}' 는 10진수 {}로 변환됩니다.".format(y, int(y, 16)))
print("int({1})은 {0} {1}을 {2} {3}로 변환됩니다.".format(type(z), z, type(int(z)),int(z)))
print("int({1})은 {0} {1}을 {2} {3}로 변환됩니다.".format(type(x), x, type(int(x)),int(x)))

print("*****************객체 조사를 위한 함수*****************")
# 16. dir()
# 인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은 속성 정보를 리스트 객체로 반환
# 인자를 전달하지 않고 호출하면 현재 지역스코프에 대한 정보를 리스트 객체로 반환

print("dir() => {}".format(dir()))
# 지역 스코프에 대한 정보를 리스트 객체로 반환

data_str = "Hello, Python!"
print("dir(data_str) => {}".format(dir(data_str)))
# 문자열이 가지고 있는 많은 메소드 정보를 리스트 객체에 담아 반환

data_list = [10, 20, 30, 40, 50]
# dir(data_list) 정수형 리스트 객체가 가지고 있는 메소드 정보들을 리스트 객체에 담아 반환

data_dict = {"key1" : 10, "key2": 20, "key3": 30}
# dir(data_dict) 객체가 가지고 있는 메소드 정보들을 리스트 객체에 담아 반환


print("============================================")
# 17. globals()
# 현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환 ==> 전역 변수와 함수, 클래스의 정보 포함
# locals() : 현재의 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수 ==> 매개변수 포함한 지역변수와 중첩함수의 정보 포함
class MyClass:
    pass

def test_fn(param):
    def inner_fn():
        pass
    val1 = 5
    val2 = 8
    for item in locals().items(): # Locals함수가 반환한 딕셔너리 객체에 대해 Items 함수로 리스트 객체를 얻음
        print("\t{} : {}".format(item[0], item[1])) # 첫 번쨰 항목인 키를, 두 번째 항목인 값을 접근해 지역 정보 출력
value1 = 10
value2 = 20
obj1 = MyClass()

g = dict(globals()) # globals 함수가 반환한 dict 객체의 현재 상태를 복사해 g에 저장
print("globals()") # g의 items함수로 반환된 리스트 객체를 얻음
for item in g.items():
    print("\t{} : {}".format(item[0], item[1])) # 튜플객체인 각 항목에 대해 키, 값 접근해 전역 정보 출력

print("\n\nlocals()") # test_fn 함수를 호출하면서 인자 값 10을 전달해서 4행~10행까지 차례대로 실행
test_fn(10)

# 18. id()
# 인자로 전달된 객체의 고유 주소(참조값)을 반환하는 함수
x = 10
print("{} x의 주소 값: {}".format(type(x), hex(id(x))))
# 이러한 고유 주소의 값은 대부분 16진수를 쓰기 때문에 hex함수를 이용

y = 10
print("{} y의 주소 값: {}".format(type(y), hex(id(y))))
# 두 결과로 10이라는 값을 참조하는 x와 y는 동일한 주소를 참조하는 것을 확인 가능

z = "10"
print("{} z의 주소 값: {}".format(type(z), hex(id(z))))
# String 10과 Int 10의 값은 다른 값을 반환'

# 19. isinstance()
# 첫 번째 인자로 전달된 객체가 두 번째 인자로 전달된 클래스의
# 인스턴스인지에 대한 여부를 True/False로 반환하는 함수
# issubclass()
# 첫 번째 인자로 전달된 객체가 두 번째 인자로 전달된 클래스의
# 서브클래스인지에 대한 여부를 True/False로 반환하는 함수

class Parent:
    pass

class Child(Parent): # Parent클래스를 상속
    pass

p=Parent()
c=Child()

print("p 객체는 Parent 클래스의 인스턴스입니까? {}".format(isinstance(p, Parent)))
print("c 객체는 Child 클래스의 인스턴스입니까? {}".format(isinstance(c, Child)))
print("c 객체는 Parent 클래스의 인스턴스입니까? {}".format(isinstance(c, Parent)))
print("p 객체는 Child 클래스의 인스턴스입니까? {}".format(isinstance(p, Child)))
print("Child 클래스는 Parent 클래스의 서브클래스입니까? {}".format(issubclass(Child, Parent)))

print("**********************실행 관련 함수************************")
# 20. eval()
# 실행 가능한 표현식의 문자열을 인자로 전달받아 해당 문자열의 표현식을 실행한 결과값을 반환하는 함수
expr = "2 + 5 * 3"
print("{} => {}".format(expr, eval(expr)))

expr = "'hello, python!'.upper()"
print("{} => {}".format(expr, eval(expr)))


# Exercise 01
data_list = list(range(1,21))
print("data_list : {}".format(data_list))

map_list = list(map(lambda x: x+5, data_list))
print("data_list에 대한 map 함수의 적용 결과 : {}".format(map_list))

filter_list = list(filter(lambda x: x%3 == 0, map_list))
print("map_list에 대한 filter 함수의 적용 결과 : {}".format(filter_list))

map_str = input("항목 x에 대하여 적용할 표현식 입력 : ")
map_list = list(map(lambda x: eval(map_str),data_list))
print("data_list에 대한 입력 map 함수의 적용 결과 : {}".format(map_list))

filter_str = input("항목 x에 대하여 필터링할 조건의 표현식을 입력 : ")
filter_list = list(map(lambda x: eval(filter_str),map_list))
print("data_list에 대한 입력 filter 함수의 적용 결과 : {}".format(filter_list))

