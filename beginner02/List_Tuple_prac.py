# 6273 List 01
scores = [(90, 80), (85, 75), (90, 100)]
print(scores)

for idx, score in enumerate(scores):
    sums = score[0] + score[1]
    avg = sums / 2
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(idx + 1, sums, avg))

# 6275 List 02
vowels = 'aeiou'

notE = 'e'
data03 = []

data_str02 = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
data_list02 = [item for item in data_str02 if item not in vowels]
print(data_list02)
print(''.join(data_list02))

# 6276 List 03
'''
다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를

제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.
'''
data_list03 = []

for i in range(2,10):
    dataSample = []
    for j in range(1,10):
        number = i*j
        if number % 3 != 0 and number % 7 != 0:
            dataSample.append(number)
    data_list03.append(dataSample)

print(data_list03)

# 6277 List 04
'''
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
'''
'''
input04 = []
sums, average= 0, 0
for i in range(5):
    num = int(input("prac04 입력 : "))
    sums += num
    input04.append(num)

average = sums / len(input04)

print(input04, " 평균은 : ", average)
'''

list04 = [int(x) for num in range(5) for x in input("리스트 04 입력 : ").split('\n')]
print(list04)
avg, sums = 0, 0
for i in range(len(list04)):
    sums += list04[i]

avg= sums/len(list04)
print(list04, " 평균은 : ", avg)

# 6280 List 06
list06 = []
num = int(input("리스트 06번 입력 : "))
for i in range(1, num+1):
    if num%i == 0 :
        list06.append(i)
print(list06)

# 6281 List 07
num = int(input("리스트 07번 입력 : "))
factors = [n for n in range(1, num+1) if num%n==0]
print(factors)

# 6282 List 08
# 내포 기능도 가능...
list08 = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
result = []
for i in range(len(list08)):
    if list08[i] % 2 == 0:
        result.append(list08[i])
print(result)

# 6286 List 11
list11 = [1,1]
[list11.append(list11[i-1] + list11[i-2]) for i in range(2, 10)]

print(list11)

# 6288 List 12
'''

리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나
5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.

'''
list12 = list(range(1,21))
result = []
print(list12)
for i in range(len(list12)):
    if (list12[i]%3 !=0) or (list12[i]%5 != 0) :
        result.append(list12[i]**2)

print(result)
