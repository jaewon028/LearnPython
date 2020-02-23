# 6308 InnerFunction 01
from datetime import date

name = input("이름입력 : ")
age = int(input("나이 입력 : "))
now = date(2020, 2, 22).year

print("{}(은)는 {}년에 100세가 될 것입니다.".format(name, now - age + 101))

# 6311 InnerFunction 04
stringData = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

stringList = list(stringData)
print(stringList)

list1 = list(map(lambda x: (x == "A") * 4, stringData))  # Python에서는 True와 False가 1과 0으로 표현되기때문에 가능한 식
list2 = list(map(lambda x: (x == "B") * 3, stringData))
list3 = list(map(lambda x: (x == "C") * 2, stringData))
list4 = list(map(lambda x: (x == "D") * 1, stringData))
print(sum(list1) + sum(list2) + sum(list3) + sum(list4))

# 6313 InnerFunction 06
ASCII = int(input("아스키코드로 입력받을 숫자 입력 : "))
print("ASCII {0} => {1}".format(ASCII, chr(ASCII)))

# 6314 InnerFunction 07
data_list = list(range(1, 11))

funcEven = list(filter(lambda x: x % 2 == 0, data_list))
print("{}".format(funcEven))

# 6315 InnerFunction 08
funcSquare = list(map(lambda x: x ** 2, data_list))
print("{}".format(funcSquare))

# 6316 InnerFunction 09
funcSquareEven = list(map(lambda x: x ** 2, funcEven))
print("{}".format(funcSquareEven))

# 6317 InnerFunction 10
max_list = [3, 5, 4, 1, 8, 10, 2]

'''
2번째 maximize 방법
def maxi(*args):
    max0 = 0
    for i in args:
        if (max0 < i):
            max0 = i
    return max0

'''


maximized = max(*max_list)
print('max{} => {}'.format(tuple(max_list), maximized))

# 6318 InnerFunction 11

stringDict = dict(a=0, b=1, c=2, d=3, e=4, f=5)
'''
2번째 방법
a = 'abcdef'
lis = list(a)
dic = {}
l = len(lis)
for i in range(l):
    dic[lis[i]] = i

for key, value in sorted(dic.items()):
    print('{}: {}' .format(key, value))
'''
for key, value in stringDict.items():
    print("{}: {}".format(key, value))