
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