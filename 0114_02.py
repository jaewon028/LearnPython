# -*- coding: utf-8 -*-

a = "파이썬"
b = "프로그래밍"
c = "기본"

print(a)
print(b)
print(c)

print("백슬래시\\")

d = "이름: %s" %"홍길동"
print(d)
e = "%c => %d" %(97, 97)
print(e)
print("%10.2f" %3.141592)

print("%010.2f" % 3.141592)

print("이름 : {0}, 나이 : {1} 세".format("홍길동", 20))

student = {"홍길동","이순신","강감찬","홍길동"}
print(student)
print(len(student))

student |= {"을지문덕","이순신"}
print(student)

student ={"임꺽정",30}
print(student)

dogs = {1:"골든리트리버", 2:"진돗개", 3:"보더콜리"}

print(dogs[1])
dogs[2] = "레브라도리트리버"
print(dogs)
dogs["4"] = "알래스카말라뮤트"
print(dogs)
print(dogs["4"])
# 이건 에러 발생 print(dogs[4])

print("\n")

obj = None
if obj: #none객체는 false로 평가
    print("obj는 None이 아닙니다.")
else:
    print("obj는 none입니다.")

