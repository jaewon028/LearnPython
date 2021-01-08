if __name__ == "__main__":
    num = int(input())
    hansoo = 0

    for i in range(1, num+1):
        if i < 100:
            hansoo += 1
        else:
            list_num = list(map(int, str(i)))
            if list_num[2] - list_num[1] == list_num[1] -list_num[0]:
                hansoo += 1

    print(hansoo)