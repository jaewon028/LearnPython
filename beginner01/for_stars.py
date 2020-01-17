# -*- coding : utf-8 -*_

# 결과1 for문 or while문


'''
for i in range(1,5):
    for j in range(1,i):
        print("*", end='')
    print()


for i in range(0,5):
    for j in range(0,i):
        print("{0} and {1}".format(i,j))
'''


for i in range(1,5): # 1,2,3,4
    print("*" * i)

for i in range(0,5):
    print(i)

num = 1
while num <=4 :
    print("*" *num)
    num += 1

print("-------------결과2 for문 ---------------")
#결과 2 for 문
for i in range(1,3):
    for j in range(1,5):
        print("*" * j)

print("-------------결과2 while문 ---------------")
#결과 2 while문
num = 1;
num2 = 1;
while num<=2:
    while num2<=4:
        print("*" * num2)
        num2+=1
    num +=1
    num2 = 1

print("--------------결과3 for문---------------")
#결과 3 while문
i, k = 5, 1
while i>=0:
    print("{0}{1}".format(" " *i, "*" * (2*k-1)))
    i-=1
    k+=1
