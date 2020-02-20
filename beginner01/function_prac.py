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
memo = {1: 1, 2: 1}
fibonacci_list = int(input("fibonacci num input : "))


def fibo(n):
    if n not in memo:
        memo[n] = fibo(n - 1) + fibo(n - 2)
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
li = [1, 2, 3, 4, 3, 2, 1]

new_list = list()


def newlist(list05):
    global new_list
    for n in range(len(list05)):
        num = list05[n]
        if num not in new_list:
            new_list.append(num)


print(li)
newlist(li)
print(new_list)

# 6325 function 06
li06 = [2, 4, 6, 8, 10]


def search_list06(value, list06):
    if value not in list06:
        print("{0} => False".format(value))
    if value in list06:
        print("{0} => True".format(value))


print(li06)
search_list06(5, li06)
search_list06(10, li06)


# 6326 function 07
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


factorial_input = int(input("팩토리얼 숫자 입력 : "))
print("{}".format(factorial(factorial_input)))

# 6327 function 08
input08 = input("square num : ")


def square(value):
    num = value ** 2
    return num


num1, num2 = map(int, input().split(','))
print("square({0}) => {1}".format(num1, square(num1)))
print("square({0}) => {1}".format(num2, square(num2)))