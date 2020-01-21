#반복문01
#01-1. 랜덤함수 이용
import random
stu_num = 5
for i in range(stu_num):
    score = random.randrange(0, 101)
    if(score<60):
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i+1,score))
    elif(60<=score<=100):
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i+1,score))

#01-2. 리스트(배열 이용)
'''
list = [88, 30, 61, 55, 95]
for i in list:
    if(list[i]>=60):
        print('{}번 학생은 {}점으로 합격입니다.' .format(i+1, list[i]))
    else:
        print('{}번 학생은 {}점으로 불합격입니다.' .format(i+1, list[i]))
'''

list = [99,22,11,40]
for i in list:
    print("i는 {}".format(i))
#    print("list는 {}".format(list[i]))


#6231 for 02
for i in range(1,101):
    print(i)

#6234 for 03
for i in range(2, 101, 2):
    print(i, end=" ")
print()

#6238 for 04
for i in range(1, 101, 2):
    if(i==99):
        print(i)
        break
    print(i, end=", ")

#6240  for 05
sum = 0;
for i in range(1, 101):
    if( i % 3 ==0 ):
        sum+= i
print("1부터 100사이의 숫자 중 3의 배수의 총합: {}".format(sum))

#6242 for 06
bloodType = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
typeA, typeB, typeO, typeAB = 0, 0, 0, 0;
for n in bloodType:
    if(n == 'A'):
        typeA += 1
    elif(n == 'B'):
        typeB += 1
    elif(n == 'O'):
        typeO += 1
    elif(n == 'AB'):
        typeAB += 1
print("{{'A': {}, 'O':{}, 'B': {}, 'AB': {}}}".format(typeA, typeO, typeB, typeAB)) # 중괄호 출력 방법 : {{

#6244 for 07
li = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum=0
while len(li) > 0 :
    if(li[0] >= 80):
        sum = sum + li.pop(0)
    else:
        li.pop(0)
print(sum)

