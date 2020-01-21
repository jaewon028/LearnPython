dan = int(input("단을 입력하세요: "))
for i in range(1, 10, 1): # 튜플 객체 대신 range() 함수 이용
    print("{0} x {1} = {2:>2}".format(dan, i, dan * i)) # :>2 는 오른쪽으로 2칸 폭을 띄음을 의미

'''
range() 함수의 인자 값
첫 번째 인자 값은 범위에 포함되고, 두 번째 인자로 전달된 값은 범위에 포함되지 않음
두 번째 인자는 생략할 수 없으며, 첫 번째 인자와 세 번째 인자는 생략가능
인자를 생략할 경우 첫 번째의 기본 값은 0, 두번째 인자의 기본 값은 1
range(0, 10, 1) #0,1,2,3,4,5,6,7,8,9
rnage(10,1)
range(10)
위 세개는 모두 동일한 코드
range(1, 10, 2) # 1, 3, 5, 7, 9
rnage(10, -1 -2) # 10, 8 , 6, 4, 2
'''

dogs = {1: "골든리트리버", 2: "진돗개", 3: "보더콜리"} # 딕셔너리 객체
for key in dogs :   # 사전 객체 dogs를 사용하므로 항목의 키 정보 1,2,3이 차례로 대입
    print("{0} : {1}".format(key, dogs[key])) # 첫번째 반복에서 eky에 1이 대입되면 str.format()함수의 첫 번쨰 인자값으로 1, 두전째 인자로 골든 리트리버 전달

for key, value in dogs.items(): # <class 'dict_itmes'> 객체 사용
    print("{0} : {1}".format(key, value)) # 변수 key와 변수 value에 키 정보와 값 정보 차례대로 대입 후 print()함수 실행

str = "Python"
for c in str:
    print("{0}".format(c))

#리스트 객체를 이용한 총점 구하기 코드
scores = [100, 95, 88, 98]
total =0

for score in scores:
    total += score

print("총점 : {0}".format(total))

#2~9단 구구단
dan = range(2,10) # 2 부터 9 까지
num = range(1, 10) # 1 부터 9 까지

for i in dan: # 2부터
    for k in num: # 1부터
        print("{0} X {1} = {2:>2}".format(i, k, i*k))
        if k==9:
            print()

#기본 while
dan2 = 4
i=1
while i < 10:
    print("{0} X {1} = {2:>2}".format(dan2, i, dan2*i))
    i += 1

#리스트 객체를 이용한 총점 구하기 while
scores = [100, 95, 88, 98]
total =0
cnt = len(scores)
i = 0

while i < cnt:
    total += scores[i]
    i+=1

print("총점 : {0}".format(total))

#break문 예제
answer =""

while True:
    answer = input("명령을 입력하세요.\n 'q'를 입력하면 프로그램이 종료됩니다 . :")
    if answer == "q":
        break
    print("'{0}'를 입력하셨습니다.".format(answer))
print("프로그램을 종료합니다")

#continue문 예제
numlist = [1,2,3,4,5,6,7,8,9,10]
total = 0

for n in numlist:
    if n%3 ==0:
        continue;
    total += n
print("3의 배수를 제외한 총합 : {0}".format(total))