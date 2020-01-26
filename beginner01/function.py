# 매개변수와 반환 값이 있는 함수
def func_parameters_retrun(x, y, z):
    print("매개변수로 전달된 값은 {}, {}, {} 입니다.".format(x, y, z))
    print("매개변수와 변환값이 있는 함수입니다.")
    return "Hello, Python!"


ret_val = func_parameters_retrun(1, 2, 3)
print("func_parameters_return() 함수가 변환한 값: {}".format(ret_val))

print("---------------------------------------")


# 매개변수는 없고, 반환 값만 있는 함수
def func_noparameters_retrun():
    print("매개변수와 변환값이 없는 함수입니다.")
    return "Hello, Python!"


ret_val = func_noparameters_retrun()
print("func_noparameters_return() 함수가 변환한 값: {}".format(ret_val))

print("---------------------------------------")


# 매개변수는 있고, 반환 값이 없는 함수
def func_parameters_noreturn(x, y, z):
    print("매개변수로 전달된 값은 {}, {}, {} 입니다.".format(x, y, z))
    print("매개변수와 변환값이 있는 함수입니다.")


func_parameters_noreturn(2, 3, 4)

print("---------------------------------------")


# 매개변수와 반환 값이 없는 함수
def func_noparameters_noreturn():
    print("매개변수와 반환값이 없는 함수입니다.")


func_noparameters_noreturn()


# 언팩 연산자를 사용하는 튜플 형식의 가변 매개변수
def calc_sum(*params):  # 매개변수에 인자 값들이 튜플 형식으로 전달
    total = 0
    for val in params:  # 반복
        total += val
    return total


ret_val = calc_sum(1, 2)
print("calc_sum 함수 반환 값 : {}".format(ret_val))
ret_val = calc_sum(1, 2, 3)
print("calc_sum 함수 새로운 반환 값: {}".format(ret_val))


# 주의! 가변형 매개변수는 하나만 지정할 수 있으며, 가변형 매개변수를 가장 마지막 매개변수로 지정해야 부작용 없이 사용할 수 있음.

# 명시적 매개변수와 가변 매개변수의 혼합 사용
def calc_sum(precision, *params):  # 첫 매개변수 precision에 인자 값이 가장 먼저 전달. 나머지 인자값은 params에 튜플형식으로 전달
    if precision == 0:
        total = 0
    elif 0 < precision < 1:
        total = 0.0  # 부동소수점 0.0으로 초기화

    for val in params:
        total += val
    return total


ret_val = calc_sum(0, 1, 2)
print("calc_sum(0,1,2) 함수가 반환한 값 : {}".format(ret_val))
ret_val = calc_sum(0.1, 1, 2)
print("calc_sum(0.1,1,2) 함수가 반환한 값 : {}".format(ret_val))


# 언팩 연산자를 사용하는 튜플 형식의 반환 값
def calc_sum(precision1, precision2, *params):  # 첫 매개변수 precision에 인자 값이 가장 먼저 전달. 나머지 인자값은 params에 튜플형식으로 전달
    if precision1 == 0:
        total1 = 0
    elif 0 < precision1 < 1:
        total1 = 0.0  # 부동소수점 0.0으로 초기화

    if precision2 == 0:
        total2 = 0
    elif 0 < precision2 < 1:
        total2 = 0.0

    for val in params:
        total1 += val
        total2 += val

    return total1, total2  # 튜플을 변환해서 하나 이상의 값을 반환 가능


ret_val = calc_sum(0, 0.1, 1, 2)
print("calc_sum(0, 0.1,1,2) 함수가 반환한 값 : {}, {}".format(*ret_val))
print("calc_sum(0, 0.1,1,2) 함수가 반환한 값 : {}, {}".format(ret_val[0], ret_val[1]))

print()
# 키워드 언팩 연산자 **
'''
매개변수의 개수를 가변적으로 사용할 수 있도록 함
키워드 인자들을 전달해 매개변수를 딕셔너리 형식으로 처리함
'''


def use_keyword_arg_unpacking(**params):  # 키=값 형식의 인자 값들이 params 매개변수에 딕셔너리 형식으로 전달
    for k in params.keys():  # 매개변수 params에서 params.key()함수를 통해 키 리스트를 구함
        print("{}: {}".format(k, params[k]))  # 키는 전달된 매개변수 이름, 값은 전달된 인자 값


print("use_keyword_arg_unpacking()의 호출")
use_keyword_arg_unpacking(a=1, b=2, c=3)

print("===========================================")


# 중요! 매개변수에 전달할 인자 값이 생략되었다면? ====> 사용할 기본 값 지정!
def calc(x, y, operator="+"):  # "+"를 기본값으로 설정. operator에 넣을 값을 생략해도 +가 기본
    if operator == "+":
        return x + y
    else:
        return x - y


ret_val = calc(10, 5, "+")
print("calc(10, 5, '+')의 결과 값 : {}".format(ret_val))

ret_val = calc(10, 5)
print("calc(10, 5)의 결과 값 : {}".format(ret_val))
ret_val = calc(10, 5, "-")
print("calc(10, 5, '-')의 결과 값 : {}".format(ret_val))
ret_val = calc(10, 5, "*")
print("calc(10, 5, '*')의 결과 값 : {}".format(ret_val))

print("======================================")


# 중첩 함수 : 함수 내에 중첩함수를 선언해 사용 가능
# 1. 중첩함수를 퐇마하는 함수 내에서만 호출이 가능함
# 2. 중첩함수를 퐇마하는 함수의 스코프에도 접근이 가능함
def calc(operator_name, x, y):
    return operator_name(x, y)


def plus(op1, op2):
    return op1 + op2


def minus(op1, op2):
    return op1 - op2


ret_val = calc(plus, 10, 5)
print("calc(plus, 10, 5)의 결과 값 : {}".format(ret_val))

ret_val = calc(minus, 10, 5)
print("calc(minus, 10, 5)의 결과 값: {}".format(ret_val))

print("=====================================")
# 람다식
'''
 Lambda 매개변수 : 반환값 
 1. 변수에 저장해 재사용이 가능한 함수처럼 사용
 2. 기존의 함수처럼 매개변수의 인자로 전달함
 3. 함수의 매개변수에 직접 인자로 전달함
'''
def calc2(operator_fn, x, y):
    return operator_fn(x, y)

ret_val = calc2(lambda a, b: a+b, 10, 5)
print("calc2(lambda a, b: a+b, 10, 5)의 결과 값: {}".format(ret_val))

ret_val = calc2(lambda a, b: a-b, 10, 5)
print("calc2(lambda a, b: a-b, 10, 5)의 결과 값: {}".format(ret_val))



print("=======================================")
# 클로저
'''
 1. 중첩함수에서 중첩함수를 포함하는 함수의 scope에 접근 가능
 2. 중첩함수 자체를 반환값으로 사용한다면?
    1) 정보 은닉 구현 가능
    2) 전역변수의 남용 방지
    3) 메서드가 하나밖에 없는 객체를 만드는 것보다 우아한 구현 가능
'''
def outer_func():
    id = 0

    def inner_func():
        nonlocal id # 변수 id가 중첩함수인 inner_func 함수의 지역변수가 아님
                    # 변수 id 접근시 outer_func 함수 스코프에서 찾게 만듦
        id+=1
        return id
    return inner_func # 주의!! 여기서 inner_func() 함수호출이 아닌 함수에 대한 참조를 반환함에 주의하자

make_id = outer_func()
print("make_id() 호출의 결과: {}".format(make_id()))
print("make_id() 호출의 결과: {}".format(make_id()))
print("make_id() 호출의 결과: {}".format(make_id()))


print("===========================================")
# 함수를 활용한 원의 둘레와 면적 구하기
# 반지름 입력, 원의 면적 계산, 원의 둘레 계산
def input_radius():
    radius_str = input("반지름을 입력하세요: ")
    return float(radius_str)

def calc_circle_area(r):
    return 3.14 * r * r

def calc_circumference(r):
    return 2 * 3.14 * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumference = calc_circumference(radius)
print("원의 면적 : {0:0.2F}, 원의 둘레: {1:0.2F}".format(circle_area, circumference)) # 0.2F 소숫점 둘 째 자리까지 계산
