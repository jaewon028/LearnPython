# 1. 표준 모듈
# import

# - * - coding: utf-8 - * -
import math # math 모듈 참조
print("math.radians(90) = {}".format(math.radians(90))) #각도를 라디안 변환 값으로 반환

print("math.ceil(3.2) = {}".format(math.ceil(3.2))) # 인자로 전달된 숫자보다 큰 값 중 최소 정수 반환

print("math.floor(3.2) = {}".format(math.floor(3.2))) # 인자로 전달된 숫자보다 작은 값 중 최대 정수

print("math.pi = {}".format(math.pi)) # 3.14 원주율 값 저장

# import 모듈명 as 별칭
# import math as m
'''
print("m.radians(90) = {}".format(m.radians(90))) #각도를 라디안 변환 값으로 반환

print("m.ceil(3.2) = {}".format(m.ceil(3.2))) # 인자로 전달된 숫자보다 큰 값 중 최소 정수 반환

print("m.floor(3.2) = {}".format(m.floor(3.2))) # 인자로 전달된 숫자보다 작은 값 중 최대 정수

print("m.pi = {}".format(m.pi)) # 3.14 원주율 값 저장

'''

# from ~ import ~  : 선택적 로
# from math import * : 모듈 혹은 패키지가 가지고 있는 함수, 값 등의 모든 정보를 로딩해서 사용

# from math import radians, ceil, floor, pi : 선택적으로 함수와 값을 로딩해 사용
# 명시적으로 선언해 사용하면, 해당 함수가 어느 모듈에서 로딩되어 사용됐는지 명확하게 알 수 있으므로 사용 권장.
