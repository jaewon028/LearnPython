# swea 4828

'''

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.


[입력]

첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

1 2 3 4 5

입력
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175


출력
#1 630739
#2 740510
#3 838110
'''

T = int(input("#T"))
N = int(input("#N"))
List_ai = []
for i in range(N):
    ai = int(input("ai"))
    List_ai.append(ai)

# print(List_ai)
# print(List_ai.pop())

# def max_num(aa):
#     list_pop = aa.pop()
#     max_value = list_pop
#     for i in aa:
#         if i.pop() > max_value:
#             max_value = i.pop()
#         else:
#             max_value = list_pop
#
#     print("최대값 : {} ".format(max_value))

def maxNum(bb):
    max_value = bb[0]
    numberOfMax = max_value
    for i in bb:
        if i >= numberOfMax:
            numberOfMax = i

    return numberOfMax


print(" max Num : {}".format(maxNum(List_ai)))