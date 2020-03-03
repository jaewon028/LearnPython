'''
 SET : 중복되지 않는 데이터를 만들기 위해 사용하는 자료구조.
 DICTIONARY : 키 데이터와 관련된 데이터를 연결한 자료구조.
 둘 다 반복형 자료구조. 데이터 중복 허락하지 않음.


 셋 : 중괄호 안에 서로 다른 자료형의 유일한 값을 콤마로 구분.
 하나 이상 저장할 수 있는 컬렉션 자료형 중 하나
 인덱스 제공 X. 순서 개념 X. 중복 허용 X.

'''

# 셋의 생성
data_set = {10, 20, "파이썬", "파이썬"}
print("{} {}".format(type(data_set), data_set))

data_set = set(range(10,21,2))
print("{} {}".format(type(data_set), data_set))

data_str = "Better Tomorrow"
data_set = set(data_str)
print("{} {}".format(type(data_set), data_set))
# 문자열 원소들이 정해진 순서 없이 출력됨. 중복 문자는 하나만 저장됨.


# 셋 조작법
# 1. 셋 기본 연산 (교집합, 합집합, 차집합)

data_set1 = {1,2,2,3,4,4,5,6,7,7,7,11}
data_set2 = {2,3,5,9,11,12,15}

print("{} & {} = {}".format(data_set1, data_set2, data_set1 & data_set2)) #교집합
print("{} |& {} = {}".format(data_set1, data_set2, data_set1 | data_set2)) #합집합
print("{} - {} = {}".format(data_set1, data_set2, data_set1 - data_set2)) #차집합

print("{}.intersection({}) = {}".format(data_set1, data_set2, data_set1.intersection(data_set2)))
print("{}.union({}) = {}".format(data_set1, data_set2, data_set1.union(data_set2)))
print("{}.difference({}) = {}".format(data_set1, data_set2, data_set1.difference(data_set2)))

# 2. 셋 항목 추가
data_set = {1,2,3}

print("data_set : {}".format(data_set))
data_set.add(3)
data_set.add(4)
print("data_set : {}".format(data_set))

data_set.update({4,5,6})
print("data_set : {}".format(data_set))

# 3. 셋 항목 제거
data_set = set(range(1,11))
print("data_set : {}".format(data_set))

data_set.remove(9)
data_set.remove(2)
print("data_set : {}".format(data_set))

data_set.pop() # 첫 번째 항목 제거
print("data_set : {}".format(data_set))

data_set.clear()
print("data_set : {}".format(data_set))

# 4. 셋 항목 확인
data_set1 = {1,2,3,4,5}
data_set2 = {2,3}

print("3 in data_set1 => {}".format(3 in data_set1))
print("6 not in data_set1 => {}".format(6 not in data_set1))
# issuperset ; 더큰 집합 A가 B를 전부 포함하는 집합인지 확인.
# issubset : 슈퍼셋과 반대.
print("{}.issuperset({}) => {}".format(data_set1, data_set2,
                                       data_set1.issuperset(data_set2)))
print("{}.issuperset({}) => {}".format(data_set2, data_set1,
                                       data_set2.issubset(data_set1)))

# 5. 셋과 for 문
data_set = set(range(0,11,2))

for item in data_set:
    print("{}".format(item), end=" ")

print()

for idx, item in enumerate(data_set):
    print("[{}] => {}".format(idx, item))


# 셋 내포의 특징
data_set1 = {1,2,3,4,5}
print("data_set1 : {} {}".format(type(data_set1),data_set1))

data_set2 = {item for item in data_set1}
print("data_set2 : {} {}".format(type(data_set2),data_set2))

data_set5 = {x * y for x in data_set1 if x % 2 == 1
                    for y in data_set1 if y % 2 == 0}
print("data_set5 : {} {}".format(type(data_set5), data_set5))


print("="*80)

# 딕셔너리 : 중괄호 안에 Key : Value 형식을 가진 유일한 데이터를 구분해 하나 이상 저장할수 있는 컬렉션 자료형 중 하나
# 인데스 제공 X, 순서 개념 X, 중복 허용X

# 딕셔너리의 생성
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
}

print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict2 = dict(홍길동=20, 이순신=45, 강감찬=35)
print("data_dict2: {} {}".format(type(data_dict2), data_dict2))

data_tuple1 = (("홍길동", 20), ("이순신", 45), ("강감찬", 35))
data_dict3 = dict(data_tuple1)
print("data_dict3 : {} {}".format(type(data_dict3), data_dict3))


data_list1 = [("홍길동", 20), ("이순신", 45), ("강감찬", 35)]
data_dict4 = dict(data_list1)
print("data_dict4 : {} {}".format(type(data_list1), data_list1))

# 딕셔너리 항목 접근
print("data_dict1['홍길동'] => {}".format(data_dict1["홍길동"]))
# print("data_dict1['을지문'] => {}".format(data_dict1["을지문덕"]))  ==> 에러 발생

print("="*80)

# 1. 딕셔너리 항목 추가
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
}

print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict1["을지문덕"] = 40
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict1.update({"신사임당": 50, "유관순": 16})
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# 2. 딕셔너리 항목 변경
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
}

data_dict1["강감찬"] = 38
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict1.update({"홍길동": 25, "이순신": 48})
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# 3. 딕셔너리 항목 제거
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35,
    "을지문덕": 40
}
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

del data_dict1["강감찬"]
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict1.pop("이순신")
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

data_dict1.clear()
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

# 4. 딕셔너리 항목 확인
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
}
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

print("'홍길동' in data_dict1 => {}".format("홍길동" in data_dict1))
print("'신사임당' not in data_dict1 => {}".format("신사임당" not in data_dict1))

# 5. 딕셔너리와 for 문
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

print("{} => {}".format(type(data_dict1.items()), data_dict1.items()))
print("{} => {}".format(type(data_dict1.keys()), data_dict1.keys()))
print("{} => {}".format(type(data_dict1.values()), data_dict1.values()))

print()
for key in data_dict1:
    print("key, data_dict1[key] => '{}', {}".format(key, data_dict1[key]))

print()
for key in data_dict1.keys():
    print("key, data_dict1[key] = > '{}' {}".format(key, data_dict1[key]))

print()
for item in data_dict1.items():
    # item[0]은 키를, item[1]은 값을 읽어옴.
    print("item[0], itme[1] => '{}', {}".format(item[0], item[1]))

print()
for item in data_dict1.items():
    print("item[0], item[1] => '{}', {}".format(item[0], item[1]))

print()
for key, value in data_dict1.items():
    print("key, value => '{}', {}".format(key, value))

print()
for value in data_dict1.values():
    print("value => {}".format(value))


print("="*80)

# 딕셔너리 내포
data_dict1 = {
    "홍길동": 20,
    "이순신": 45,
    "강감찬": 35
}
print("data_dict1: {} {}".format(type(data_dict1), data_dict1))

print()
data_set1 = [item for item in data_dict1.items()]
print("data_set1: {} {}".format(type(data_set1), data_set1))

print()
data_dict2 = {key: data_dict1[key] for key in data_dict1}
print("data_dict2: {} {}".format(type(data_dict2),data_dict3))

print()
data_dict3 = {key: data_dict1[key] for key in data_dict1.keys()}
print("data_dict3: {} {}".format(type(data_dict3),data_dict3))


print()
data_dict4 = {item[0]: item[1] for item in data_dict1.items()}
print("data_dict4: {} {}".format(type(data_dict4),data_dict4))

print()
data_dict5 = {key: value for key, value in data_dict1.items()}
print("data_dict5: {} {}".format(type(data_dict5), data_dict5))



print("= " * 50 )
# 학생 및 점수 정보 저장 후 평균 점수 구하기
scores = []
count = int(input("총 학생의 수를 입력하세요 : "))

for i in range(1, count + 1):
    score = {}
    score["name"] = input("학생의 이름을 입력하세요: ")
    score["kor"] = int(input("{} 학생의 국어 점수를 입력하세요: ".format(score["name"])))
    score["mat"] = int(input("{} 학생의 수학 점수를 입력하세요: ".format(score["name"])))
    score["eng"] = int(input("{} 학생의 영어 점수를 입력하세요: ".format(score["name"])))
    scores.append(score)

for score in scores:
    total = 0
    for key in score:
        if key != "name":
            total += score[key]
    print("{0} => 총점: {1}, 평균: {2:0.2F}".format(score["name"], total, total/3))