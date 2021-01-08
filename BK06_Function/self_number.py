def d(n):
    result_sum = 0
    for i in list(str(n)):
        result_sum += int(i)

    return int(n) + result_sum

if __name__ == "__main__":
    list_result = []
    for i in range(1, 10001):
        idx = d(i)
        list_result.append(idx)

    for i in range(1, 10001):
        if i not in list_result:
            print("{0}".format(i))
