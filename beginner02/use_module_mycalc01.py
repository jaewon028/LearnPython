'''
from beginner02 import module_mycalc01, module_mycalc02

op1, op2 = 2,3

result = module_mycalc01.plus(op1, op2)
print("plus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc01.minus(op1, op2)
print("minus({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc02.multiply(op1, op2)
print("multiply({0}, {1}) => {2}".format(op1, op2, result))

result = module_mycalc02.divide(op1, op2)
print("divide({0}, {1}) => {2:.2}".format(op1, op2, result))
'''


# 모듈의 __name__ 속성
'''
실행 목적의 모듈
: _name_속성에 "_main_"문자열 값이 들어가 있음

라이브러리 목적의 모듈
: _name_속성에 모듈의 이름이 저장되어 있음
'''

def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

# 모듈로 실행되었을 때와 메인으로 실행되었을 때를 구분해 동작할 수 있음
if __name__ == "__main__": # python 명령으로 실행 ==> 실행 모듈로 동작
    print("plus(3,2) => {}".format(plus(3,2)))
    print("minus(3,2) => {}".format(minus(3,2)))