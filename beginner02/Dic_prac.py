# 6254 Dic 02
'''
다음과 같이 등록된 학생의 이름을 출력하고, 이름을 입력하면 전화번호를 출력해주는


딕셔너리 객체를 이용한 전화번호부 프로그램을 작성하십시오.

[등록된 학생]

홍길동: 010-1111-1111
이순신: 010-1111-2222
강감찬: 010-1111-3333


[프로그램]

아래 학생들의 전화번호를 조회할 수 있습니다.
홍길동
이순신
강감찬
전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.
'''
contact = {
    "홍길동": "010-1111-1111",
    "이순신": "010-1111-2222",
    "강감찬": "010-1111-3333"
}

print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for key in contact.keys():
    print(key)
nameInput = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n")
print("{0}의 전화번호는 {1}입니다.".format(nameInput, contact[nameInput]))

print("="*60)

# 6255 Dic 03
electronics = {
    "TV": 2000000,

    "냉장고": 1500000,

    "책상": 350000,

    "노트북": 1200000,

    "가스레인지": 200000,

    "세탁기": 1000000
}

elecDict = {r: electronics[r] for r in sorted(electronics, key=electronics.get, reverse=True)}
# !!!!!!    DICTIONARY.get ==> 각 키에 대한 value 값을 반환.

for idx, val in elecDict.items():
    print("{}: {}".format(idx, val))

# 6256 Dic 04
a = {'아메리카노': 2000, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}

b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

newMenu = {key: value for key, value in a.items() | b.items()}
updataeMenu = {(key, value) for key, value in newMenu.items() if value > 3000}

# Check the combined Menu
print(updataeMenu)

print("=" * 60)

# 6257 Dic 05
'''
리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다.

이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다.

리스트 fruit는 다음과 같습니다. fruit = ['   apple    ','banana','  melon']

출력
{'apple': 5, 'banana': 6, 'melon': 5}
'''
fruit = ['   apple    ','banana','  melon']

lengthFruit = []

for i in range(len(fruit)):
    lengthFruit.append(len(fruit[i].strip()))

# check each of lengths
for i in lengthFruit:
    print(i)

newLength = {}
for i in range(len(fruit)):
    newLength.update({fruit[i].strip(): lengthFruit[i]})

print(newLength)

print("=" * 70)

# 6258 DIc 06
num = int(input("딕셔너리 06번 입력 : "))
Dic06 = {i: i**2 for i in range(1, num+1)}

print(Dic06)
