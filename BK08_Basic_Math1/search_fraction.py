if __name__ == "__main__":
    num = int(input())
    i = 0
    while num > 0:
        num -= i
        i += 1

    num = i + num - 1
    res = str(num) + '/' + str(i - num)
    if i % 2 == 0:
        res = str(i - num) + '/' + str(num)

    print(res)