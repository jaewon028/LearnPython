# 3. random 모듈
# 난수를 생성하는 기능 제공
from random import random, uniform, randrange, choice, sample, shuffle, choices

print("random() => {0}".format(random()))
print("uniform{0}, {1} => {2}".format(1.0, 10.0, uniform(1.0, 10.0)))
# uniform 함수 : 지정된 범위 내의 부동소수점 난수 N 반환

start, stop, step = 1, 45, 2
# randrange 함수 : 정수 난수 N 생성
print("randrange({0}, {1}) => {2}".format(start, stop, randrange(start, stop)))
# 1<= N < 45 범위 정수 반환
print("randrange({0}) => {1}".format(stop, randrange(stop)))
# 0<= N <45 범위 정수 반환 # start 정보 생략 시 0, step 정보 생략 시 1이 기본 값
print("randrange({0}, {1}, {2}) => {3}".format(start, stop, step, randrange(start, stop, step)))

data_list = [1,2,3,4,5]
# choice() : 인자로 전달된 시퀀스 객체의 항목 중 임의 항목 반환
print("choice({0}) => {1}".format(data_list, choice(data_list)))
print("choices({0}) => {1}".format(data_list, choices(data_list, k=2)))
# choices() : 인자로 전달된 시퀀스 객체의 항목 중 임의의 K개 반환. 복원 추출 기능을 가진 시뮬함수.
print("sample({0}) => {1}".format(data_list, sample(data_list, k=2)))
# sample() : 인자로 전달된 시퀀스 객체, 혹은 set 객체 항목 중
# 임의의 k개 반환. 비복원추출 기능을 가진 시뮬레이션 함수.

shuffle(data_list)
print("data_list => {}".format(data_list))
# 인자로 전달된 시퀀스 객체의 항목을 뒤섞는 함수. 반환값 없고 객체의 항목의 순서를 뒤섞음.
