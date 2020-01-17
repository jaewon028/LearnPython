
#6218 if 01
a1 = int(input())
for i in range(a1):
    if(a1 % (i+1) ==0):
        print('{}는 {}의 약수입니다.' .format(i+1,a1));

#6219 if 02
a2 = int(input())
cnt=0
for i in range(1, a2+1):
    if(a2%i==0):
        cnt+=1
        print("{}(은)는 {}의 약수입니다.".format(i, a2))

if(cnt==2):
    print("{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.".format(a2, a2))




#6220 if 03
a3 = input()
a3Ascii = ord(a3)
if((a3Ascii >= 97) and (a3Ascii <= 122) ):
    #97<=a3Ascii<122
    print("{}는 소문자 입니다." .format(a3))



#6221 if 04
man1 = input("Man 1 = ")
man2 = input("Man 2 = ")
if(man1 == "가위"):
    if(man2 =="가위"):
        print("Result : Draw")
    elif(man2 =="바위"):
        print("Result : Man2 Win!")
    elif(man2 =="보"):
        print("Result : Man1 Win!")
elif(man1 == "바위"):
    if(man2 == "가위"):
        print("Result : Man1 Win1!")
    elif(man2 == "바위"):
        print("Result : Draw")
    elif(man2 == "보"):
        print("Result : Man2 Win!")
elif(man1 == "보"):
    if (man2 == "가위"):
        print("Result : Man2 Win!")
    elif (man2 == "바위"):
        print("Result : Man1 Win!")
    elif (man2 == "보"):
        print("Result : Draw")

#6221 if04 _ 2
Man1 = input()
Man2 = input()

RSP = ["가위", "바위", "보"]

if(Man1 == Man2):
    print("Result : Draw")
elif((Man1==RSP[0] and Man2==RSP[1]) or (Man1==RSP[1] and Man2==RSP[2]) or (Man1==RSP[2] and Man2==RSP[0])):
    print("Result : Man2 Win!")
else:
    print("Result : Man1 Win!")

# 직접 입력하는게 아니라 랜덤으로 값을 주고 싶다면...
# from random import *
#
# RSP = ["가위", "바위", "보"]
#
# Man1 = RSP[randrange(3)]
# Man2 = RSP[randrange(3)]


#6227 if 08
ans = ''

for i in range(100, 300):
    if(int(str(i)[0])%2==0 and int(str(i)[1])%2==0 and int(str(i)[2])%2==0) :
        ans += str(i) + ","
print(ans[:-1])