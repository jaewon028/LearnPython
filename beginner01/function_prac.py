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