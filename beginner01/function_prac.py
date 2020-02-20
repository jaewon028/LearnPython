# -*- coding: utf-8 -*-

# 6319 function 01
def check_Palindrome(w):
    if w == ''.join(reversed(w)):
        print(''.join(reversed(w)))
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print(''.join(reversed(w)))
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")


def check_Palindrome2(w):
    if w == w[::-1]:
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")


palindrome_input = input()
check_Palindrome(palindrome_input)

palindrome_input2 = input()
check_Palindrome2(palindrome_input2)

# 6320 function 02
player1 = input()
player2 = input()
p1_choice = input()
p2_choice = input()


def rock_scissors_paper():
    if p1_choice == p2_choice:
        print("비겼습니다!")
    elif (p1_choice == "바위" and p2_choice == "가위") or (p1_choice == "보" and p2_choice == "바위") or (
            p1_choice == "가위" and p2_choice == "보"):
        print("{}가 이겼습니다!".format(player1))
    else:
        print("{}가 이겼습니다!".format(player2))


rock_scissors_paper()

# 6321 function 03
number = int(input())


def is_prime():
    cnt = 0
    for i in range(2, number):
        if number % i == 0:
            cnt += 1
    if cnt == 0:
        print(cnt)
        print("소수입니다.")
        return True
    else:
        print(cnt)
        print("소수가 아닙니다.")
        return False


is_prime()


# 6323 function 04
memo = {1:1, 2:1}
fibonacci_list = int(input("fibonacci num input : "))
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]


fibo(fibonacci_list)
for i in range(1, fibonacci_list):
    print("{}, ".format(memo[i]), end='')
print("{}]".format(memo[fibonacci_list]))
'''
def fibonacci(n):
    if n > 2:
        fibonacci_list.append((fibonacci(n-1) + fibonacci(n-2)))
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1

fibonacci(10)
print("fibonacci 값 : {}".format(fibonacci_list))

'''


# 6324 function 05
li = [1,2,3,4,3,2,1]

new_list = list()
def newlist(li):
    global new_list
    for n in range(len(li)):
        num = li[n]
        if num not in new_list:
            new_list.append(num)

print(li)
newlist(li)
print(new_list)

