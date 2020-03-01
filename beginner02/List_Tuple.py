# 시퀀스형 : 데이터에 대해 순서를 가진 자료구조 총칭  ex) 리스트, 튜플

# 1. 리스트의 생성 및 조작법
# 리스트 : 대괄호 안에 서로 다른 자료형의 값을 콤마로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형

data_list = [10, 21.5, "파이썬", True]

print("{0} {1}".format(type(data_list), data_list))

data_list = list(range(10, 21, 2))
print("{0} {1}".format(type(data_list), data_list))

data_str = "안녕하세요"
data_list = list(data_str)
print("{0} {1}".format(type(data_list), data_list))

# 리스트 조작법
# 1. 리스트 항목 접근
data_list = [10, 20, 30, 40, 50]

print("data_list : {0}".format(data_list))

print("data_list[0] => {0}".format(data_list[0]))
print("data_list[1] => {0}".format(data_list[1]))
print("data_list[2] => {0}".format(data_list[2]))
print("data_list[3] => {0}".format(data_list[3]))
print("data_list[4] => {0}".format(data_list[4]))

# 상대적인 인덱스 리스트를 통해서도 접근 가능
print("data_list[-5] => {0}".format(data_list[-5]))
print("data_list[-4] => {0}".format(data_list[-4]))
print("data_list[-3] => {0}".format(data_list[-3]))
print("data_list[-2] => {0}".format(data_list[-2]))
print("data_list[-1] => {0}".format(data_list[-1]))

# 범위 지정 가능
print("data_list[0:3] => {}".format(data_list[0:3]))
print("data_list[-5:-2] => {}".format(data_list[-5:-2]))

# 인덱스 표시 가능
print("data_list.index(20) => {}".format(data_list.index(20)))

print("=" * 40)

# 리스트 기본 연산
data_list1, data_list2 = [10, 20, 30], [40, 50]

print("data_list1: {} {}".format(hex(id(data_list1)), data_list1))
print("data_list2: {} {}".format(hex(id(data_list2)), data_list2))

print("{} + {} => {}\n".format(data_list1, data_list2, data_list1 + data_list2))

print("data_list1: {} {}".format(hex(id(data_list1)), data_list1))
print("data_list2: {} {}".format(hex(id(data_list2)), data_list2))

print("{} *2 => {}".format(data_list1, data_list1 * 2))
print("{} *3 => {}\n".format(data_list2, data_list2 * 3))

print("=" * 50)

# 리스트 항목 추가
print("data_list: {}".format(data_list))

data_list.append(50) # 반환값 : None
data_list.append(60)
print("data_list: {}".format(data_list))

data_list.insert(2, 20)
print("data_list: {}".format(data_list))

data_list.extend([70,80])
data_list.append([90,100]) # 항목 안에 항목을 추가
print("data_list: {}".format(data_list))

print("=" * 50)

# 리스트 항목 변경
data_list = [10,20,30,40]

data_list[2] = 29
print("data_list: {}".format(data_list))

data_list[1:3] = [12, 15]
print("data_list: {}".format(data_list))

data_list[1:3] = [12, 15, 20]
print("data_list: {}".format(data_list))

data_list[2:3] = [31, 25]
print("data_list: {}".format(data_list))

print("=" * 50)

# 리스트 항목 제거
data_list = [10,20,30,40,50,60,70,80,90,100]
del data_list[2]
print("data_list: {}".format(data_list))

del data_list[3:5]
print("data_list: {}".format(data_list))

data_list.pop(5)
print("data_list: {}".format(data_list))

data_list.remove(100)
print("data_list: {}".format(data_list))

data_list.clear()
print("data_list: {}".format(data_list))

print("=" * 50)

# 리스트 항목 확인
data_list = [10,20,30,40,50,60,70,80]

print("50 in data_list => {}".format(50 in data_list)) # 리스트 객체에 해당항목 있는지 검사
print("50 not in data_list => {}".format(50 not in data_list))
print("data_list.count(50) => {}".format(data_list.count(50)))
print("data_list.count(55) => {}".format(data_list.count(55)))

print("=" * 50)

# 리스트와 for 문
data_list = list(range(0, 11, 2))

for item in data_list:
    print("{}".format(item), end=" ")
print()

for idx, item in enumerate(data_list):
    print("data_list[{}] = > {}".format(idx, item))

print("*" * 80)

# 리스트 내포
data_list1 = [1,2,3,4,5]
print("data_list1: {} {}".format(type(data_list1), data_list1))

data_list2 = [] # 빈 리스트
for item in data_list1:
    data_list2.append(item) # datalist1의 모든 항목을 datalist2의 항목으로 추가
print("data_list2: {} {}".format(type(data_list2), data_list2))

data_list3 = [item for item in data_list1]
# 리스트 내포 기능을 사용하여 datalist1과 동일한 항목을 가진 datalist3 리스트 객체 생성
print("data_list2: {} {}".format(type(data_list3), data_list3))

data_list4 = []
for item in data_list1:
    if item % 2 == 1:
        data_list4.append(item)
print("data_list4: {} {}".format(type(data_list4), data_list4))

data_list5 = [item for item in data_list1 if item % 2 == 1]
print("data_list5: {} {}".format(type(data_list5), data_list5))

data_list6 = [item for item in data_list1 if item % 2 == 0]
print("data_list6: {} {}".format(type(data_list6), data_list6))

data_list7 = []
for x in data_list1:
    if x%2 == 1:
        for y in data_list1:
            if y%2 == 0:
                data_list7.append(x * y)

print("data_list7: {} {}".format(type(data_list7), data_list7))

data_list8 = [x * y for x in data_list1 if x%2 ==1
                    for y in data_list1 if y%2 ==0]
print("data_list8: {} {}".format(type(data_list8), data_list8))

data_str = "Hello, Python!"
data_list9 = [item.lower() for item in data_str]
print("data_list9: {} {}".format(type(data_list9), data_list9))


print("*" * 80)

# 튜플의 생성 및 조작법
# 튜플: 중괄호 안에 서로 다른 자료형의 값을 콤마로 구분해 하나 이상 저장할 수 있는 컬렉션 자료형
# !!!! 한 번 저장된 항목은 변경 불가 !!!!


data_tuple = (10, 21.5, "파이썬", True)
print("{} {}".format(type(data_tuple), data_tuple))

data_tuple = tuple(range(10, 21, 2))
print("{} {}".format(type(data_tuple), data_tuple))

data_str = "안녕하세요"
data_tuple = tuple(data_str)
print("{} {}".format(type(data_tuple), data_tuple))

print("*" * 80)

# 튜플 조작법
# 1. 튜플 항목 접근
data_tuple = (10,20,30,40,50)
print("data_tuple[0] => {}".format(data_tuple[0]))
print("data_tuple[1] => {}".format(data_tuple[1]))
print("data_tuple[2] => {}".format(data_tuple[2]))
print("data_tuple[3] => {}".format(data_tuple[3]))
print("data_tuple[4] => {}".format(data_tuple[4]))

print("data_tuple[-5] => {}".format(data_tuple[-5]))
print("data_tuple[-4] => {}".format(data_tuple[-4]))
print("data_tuple[=3] => {}".format(data_tuple[-3]))
print("data_tuple[=2] => {}".format(data_tuple[-2]))
print("data_tuple[-1] => {}".format(data_tuple[-1]))

#범위 접근은 리스트와 마찬가지 ( colon )

print("data_tuple.index(20) => {}".format(data_tuple.index(20)))

print("=" * 50)

# 튜플 기본 연산
data_tuple1, data_tuple2 = (10, 20, 30), (40, 50)

print("data_tuple1: {} {}".format(hex(id(data_tuple)), data_tuple1))
print("data_tuple2: {} {}".format(hex(id(data_list2)), data_tuple2))

print("data1 + 2 => {}".format(data_tuple1 + data_tuple2))

print("{} * 2 => {}".format(data_tuple1, data_tuple1 * 2))
print("{} * 3 => {}\n".format(data_tuple2, data_tuple2 *3))

print("=" * 50)

# 튜플 항목 확인
data_tuple = (10, 20, 30, 50, 50, 50, 60, 70, 80)

print("50 in data_tuple => {}".format(50 in data_tuple))
print("data_tuple.count(50) => {}".format(data_tuple.count(50)))

print("=" * 50)

# 튜플과 for 문
data_tuple = tuple(range(0, 11, 2))

for item in data_tuple:
    print("{}".format(item), end=" ")

print()

for idx, item in enumerate(data_tuple):
    print("data_tuple[{0}] => {1}".format(idx, item))

print("=" * 50)

# 튜플 내포
data_tuple1 = (1,2,3,4,5)
print("data_tuple1: {} {}".format(type(data_tuple1), data_tuple1))

data_generator1 = (item for item in data_tuple1)
print("data_generator1: {} {}".format(type(data_generator1), data_generator1))

data_tuple2 = tuple(data_generator1)
print("data_tuple2: {} {}".format(type(data_tuple2), data_tuple2))

data_tuple3 = tuple(item for item in data_tuple1 if item % 2 ==1)
print("data_tuple3: {} {}".format(type(data_tuple3), data_tuple3))

data_tuple4 = tuple(item for item in data_tuple1 if item % 2 ==0)
print("data_tuple4: {} {}".format(type(data_tuple4), data_tuple4))

data_tuple5 = tuple(x * y for x in data_tuple1 if x % 2 ==1
                            for y in data_tuple1 if y % 2 ==0)
print("data_tuple5: {} {}".format(type(data_tuple5), data_tuple5))


print("*" * 80)


# 리스트 객체로 총점 및 평균 계산 예제

scores = []
count = int(input("총 학생 수를 입력하세요 : "))

for i in range(1, count+1):
    score = []
    kor = int(input("학생{0}의 국어 점수를 입력하세요 : ".format(i)))
    score.append(kor)
    mat = int(input("학생{0}의 수학 점수를 입력하세요 : ".format(i)))
    score.append(mat)
    eng = int(input("학생{0}의 영어 점수를 입력하세요 : ".format(i)))
    score.append(eng)
    scores.append(score)

for idx, score in enumerate(scores):
    total = 0
    for s in score:
        total += s
    print("학생{0} => 총점: {1} , 평균: {2:0.2F}".format(idx+1, total, total / len(score)))